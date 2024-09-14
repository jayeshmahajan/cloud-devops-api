docker stop cloud-devops-api
docker rm cloud-devops-apir
docker build -t cloud-devops-api .
docker run -d -p 8080:8080 --name cloud-devops-api-container cloud-devops-api
docker ps
# docker tag tcpcheck-docker jayeshmahajan/tcpcheck:v0.0.1
# docker tag jayeshmahajan/tcpcheck:v0.0.1 jayeshmahajan/tcpcheck:latest
# docker push jayeshmahajan/tcpcheck:latest
