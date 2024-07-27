# TCP and HTTP/HTTPS Connection Checker

This project provides a Flask-based API to check network connections for TCP and HTTP/HTTPS protocols. It performs DNS resolution, attempts to make connections, and returns detailed results in a JSON format. 

## Features

- **TCP Connection Check**: Verifies the ability to establish a TCP connection to a specified domain and port.
- **HTTP/HTTPS Connection Check**: Verifies the ability to establish an HTTP/HTTPS connection to a specified domain.
- **DNS Resolution**: Provides detailed DNS information including CNAME and all resolved IP addresses.
- **Pretty-Printed JSON Responses**: Returns responses in a readable JSON format.
- **SSL Error Handling**: Captures and returns detailed SSL errors.

## Project Structure


tcpcheck-docker/
├── app/
│ ├── init.py
│ ├── app.py
├── requirements.txt
├── Dockerfile
├── wsgi.py


### `app/__init__.py`

Contains the main logic for DNS resolution, TCP connection checks, HTTP/HTTPS connection checks, and Flask route handlers.

### `app.py`

Defines the Flask application and routes for checking connections.

### `requirements.txt`

Lists the dependencies required for the project.

### `Dockerfile`

Defines the multi-stage Docker build process for creating a compact Docker image.

### `wsgi.py`

Entry point for running the Flask application with Gunicorn.

## Installation

### Prerequisites

- Docker
- Docker Hub account

### Building the Docker Image

Navigate to the project directory and build the Docker image:

```bash
docker build -t tcpcheck-docker .


Running the Docker Container

To run the Docker container with a specific name and using Google DNS:

```
docker run -d -p 8080:8080 --name tcpcheck-container --dns 8.8.8.8 tcpcheck-docker

```
Pushing the Docker Image to Docker Hub
Tag the Docker image:

```
docker tag tcpcheck-docker jayeshmahajan/tcpcheck:v0.0.0

```

Log in to Docker Hub:

```
docker login

```

Push the Docker image to the repository:

```

docker push jayeshmahajan/tcpcheck:v0.0.0

```

Usage
API Endpoints
Check TCP Connection
URL: /check_connection

Method: GET

Parameters:

port: Port number to check (required)
domain: Domain to check (required)
timeout: Timeout for the connection in seconds (optional, default is 5)
Example:

```
curl 'http://127.0.0.1:8080/check_connection?port=80&domain=example.com'
```

Response:

```

{
    "message": "TCP connection successful",
    "dns_result": {
        "cname": null,
        "ips": [
            "93.184.215.14"
        ]
    }
}


```

Check HTTP/HTTPS Connection
URL: /check_http_connection

Method: GET

Parameters:

protocol: Protocol to check (http or https, optional, default is https)
domain: Domain to check (required)
timeout: Timeout for the connection in seconds (optional, default is 10)
Example:

```

curl 'http://127.0.0.1:8080/check_http_connection?domain=www.google.com'

```

Respone: 

```

{
    "message": "HTTP connection successful",
    "dns_result": {
        "cname": null,
        "ips": [
            "142.250.81.238"
        ]
    }
}

```

Error Handling
The API handles various errors and returns detailed messages. Example errors include:

DNS Resolution Errors: When DNS resolution fails.
TCP Connection Errors: When the TCP connection cannot be established.
HTTP/HTTPS Connection Errors: When the HTTP/HTTPS connection fails, including SSL errors.
Example Error Response

```

{
    "error": "DNS resolution failed: A DNS label is empty."
}


```
Test Script
A test script (test/check.sh) is provided to run multiple API calls and print the results. Example usage:


sh test/check.sh


Contribution
Feel free to fork this project and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License.


