from flask import Flask, request, jsonify, Response
import socket
import dns.resolver
import ssl
import http.client
import json
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)

def get_client_ip():
    remote_addr = get_remote_address()
    if request.headers.get('X-Forwarded-For'):
        remote_addr = request.headers.get('X-Forwarded-For').split(',')[0]
    return remote_addr

# Configure the rate limiter with a single limit for simplicity
limiter = Limiter(
    key_func=get_client_ip,
    app=app,
    default_limits=["10 per minute"]
)

def dns_resolution(domain, timeout=10):
    try:
        resolver = dns.resolver.Resolver()
        resolver.lifetime = timeout  # Set the DNS resolution timeout
        cname = None
        ip_addresses = []
        cname_answers = resolver.resolve(domain, 'CNAME', raise_on_no_answer=False)
        if cname_answers.rrset:
            cname = cname_answers[0].to_text()

        ip_answers = resolver.resolve(domain, 'A', raise_on_no_answer=False)
        for answer in ip_answers:
            ip_addresses.append(answer.to_text())

        return {'cname': cname, 'ips': ip_addresses}, None
    except Exception as e:
        return None, str(e)

def tcp_connection(ip_address, port, timeout):
    try:
        sock = socket.create_connection((ip_address, port), timeout=timeout)
        sock.close()
        return 'TCP connection successful', None
    except (socket.timeout, socket.error) as e:
        return 'TCP connection failed', str(e)

def http_connection(domain, port, timeout, protocol):
    try:
        conn = http.client.HTTPSConnection(domain, port, timeout=timeout, context=ssl.create_default_context())
        conn.request("HEAD", "/")
        response = conn.getresponse()
        conn.close()
        return 'HTTP connection successful', None
    except ssl.SSLError as e:
        return 'SSL connection failed', str(e)
    except Exception as e:
        return 'HTTP connection failed', str(e)

def pretty_json(data):
    return Response(json.dumps(data, indent=4), mimetype='application/json')

@app.route('/check_connection', methods=['GET'])
@limiter.limit("10 per minute")
def check_connection():
    port = request.args.get('port')
    domain = request.args.get('domain')
    timeout = request.args.get('timeout', default=5, type=float)

    if not port or not domain:
        return pretty_json({'error': 'Port number and domain are required parameters'}), 400

    dns_result, dns_error = dns_resolution(domain, timeout)
    if dns_error:
        return pretty_json({'error': f'DNS resolution failed: {dns_error}'}), 500

    ip_address = dns_result['ips'][0] if dns_result['ips'] else None
    if not ip_address:
        return pretty_json({'error': 'No IP addresses found for domain'}), 500

    message, tcp_error = tcp_connection(ip_address, int(port), timeout)
    if tcp_error:
        return pretty_json({'message': message, 'dns_result': dns_result, 'error': tcp_error}), 500

    return pretty_json({'message': message, 'dns_result': dns_result}), 200

@app.route('/check_http_connection', methods=['GET'])
@limiter.limit("10 per minute")
def check_http_connection():
    protocol = request.args.get('protocol', 'https')
    domain = request.args.get('domain')
    timeout = request.args.get('timeout', default=10, type=float)  # Increase the default timeout

    if not domain:
        return pretty_json({'error': 'Domain is a required parameter'}), 400

    port = 443 if protocol == 'https' else 80

    dns_result, dns_error = dns_resolution(domain, timeout)
    if dns_error:
        return pretty_json({'error': f'DNS resolution failed: {dns_error}'}), 500

    ip_address = dns_result['ips'][0] if dns_result['ips'] else None
    if not ip_address:
        return pretty_json({'error': 'No IP addresses found for domain'}), 500

    if protocol == 'https':
        message, connection_error = http_connection(domain, port, timeout, protocol)
    else:
        message, connection_error = tcp_connection(ip_address, port, timeout)

    if connection_error:
        return pretty_json({'message': message, 'dns_result': dns_result, 'error': connection_error}), 500

    return pretty_json({'message': message, 'dns_result': dns_result}), 200

@app.errorhandler(429)
def ratelimit_handler(e):
    return jsonify(error="rate limit exceeded: {}".format(e.description)), 429

if __name__ == '__main__':
    app.run(debug=True, port=8080)

