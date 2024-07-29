docker stop tcpcheck-container
docker rm tcpcheck-container
docker build -t tcpcheck-docker .
docker run -d -p 8080:8080 --name tcpcheck-container tcpcheck-docker
docker ps
# docker tag tcpcheck-docker jayeshmahajan/tcpcheck:v0.0.1
# docker tag jayeshmahajan/tcpcheck:v0.0.1 jayeshmahajan/tcpcheck:latest
# docker push jayeshmahajan/tcpcheck:latest
