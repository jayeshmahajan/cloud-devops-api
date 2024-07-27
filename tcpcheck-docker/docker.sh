docker stop tcpcheck-container
docker rm tcpcheck-container
docker build -t tcpcheck-docker .
docker run -d -p 8080:8080 --name tcpcheck-container tcpcheck-docker
docker ps

