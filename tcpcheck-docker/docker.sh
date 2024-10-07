docker stop devops-cloud-api-container
docker rm devops-cloud-api-container
docker build -t devops-cloud-api-docker .
docker run -d -p 8080:8080 --name devops-cloud-api-container devops-cloud-api-docker
docker ps
# docker tag devops-cloud-api-docker jayeshmahajan/devops-cloud-api:v0.0.1
# docker tag jayeshmahajan/devops-cloud-api:v0.0.1 jayeshmahajan/devops-cloud-api:latest
# docker push jayeshmahajan/devops-cloud-api:latest
