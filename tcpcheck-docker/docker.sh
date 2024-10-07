
docker stop cloud-devops-api
docker rm cloud-devops-api
docker build -t cloud-devops-api .
docker run -d -p 8080:8080 --name cloud-devops-api-container cloud-devops-api
docker ps
# docker tag devops-cloud-api-docker jayeshmahajan/devops-cloud-api:v0.0.1
# docker tag jayeshmahajan/devops-cloud-api:v0.0.1 jayeshmahajan/devops-cloud-api:latest
# docker push jayeshmahajan/devops-cloud-api:latest
