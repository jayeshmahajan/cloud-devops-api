#!/bin/bash

urls='http://127.0.0.1:8080/check_connection?port=80&domain=example.com
http://127.0.0.1:8080/check_connection?port=800&domain=.com
http://127.0.0.1:8080/check_connection?port=800&domain=example.com
http://127.0.0.1:8080/check_connection?port=8230&domain=example.com
http://127.0.0.1:8080/check_http_connection?domain=example.com
http://127.0.0.1:8080/check_http_connection?domain=ge.com
http://127.0.0.1:8080/check_http_connection?domain=google.com
http://127.0.0.1:8080/check_http_connection?domain=www.ge.com
http://127.0.0.1:8080/check_http_connection?domain=www.google.com
http://127.0.0.1:8080/check_http_connection?protocol=http&domain=example.com
http://127.0.0.1:8080/check_http_connection?protocol=http&domain=www.ge.com
http://127.0.0.1:8080/check_connection?port=80&domain=exampasasale.com
http://127.0.0.1:8080/check_http_connection?protocol=https&domain=example.com
http://127.0.0.1:8080/check_http_connection?protocol=https&domain=expired.badssl.com
http://127.0.0.1:8080/check_http_connection?protocol=https&domain=google.com
http://127.0.0.1:8080/check_http_connection?protocol=https&domain=wrong.host.badssl.com
http://127.0.0.1:8080/check_http_connection?protocol=https&domain=www.ge.com'

for url in $urls; do
    echo "============================="
    echo "$url"
    curl $url
done

