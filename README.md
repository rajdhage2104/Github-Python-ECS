# Python Application Deployment to AWS ECS

This repository contains a Python application with CI/CD pipeline for deployment to Amazon ECS (Elastic Container Service) using EC2 instances.

## Dockerfile

```sh
FROM python:3-alpine
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./
RUN ln -sf /dev/stdout /src/app.log \
    && ln -sf /dev/stderr /src/error.log
EXPOSE 5000
ENTRYPOINT ["python3", "src/app.py"]
```

## CI/CD Pipeline

The CI/CD pipeline in this repository automates the following steps:
1. Code checkout
2. Python setup and dependency installation
3. Unit testing and code coverage
4. Docker image building
5. Security scanning with Trivy
6. Pushing the Docker image to Amazon ECR
7. Updating and registering the ECS task definition
8. Deploying the application to Amazon ECS

## ECS Deployment Setup

To deploy this application to Amazon ECS with EC2 instances, you need to set up the following:

### 1. Create Required AWS Resources via AWS Console

- **EC2 Launch Type ECS Cluster**: Create an ECS cluster with EC2 instances through the AWS console
- **EC2 Instance(s)**: Launch EC2 instances with the ECS-optimized AMI and register them to your cluster
- **ECS Service**: Create a service through the AWS console to run and maintain your tasks
- **ECR Repository**: Create an ECR repository through the AWS console to store your Docker images

The task definition is automatically created and updated by the CI/CD pipeline.

### 2. EC2 Instance Setup for ECS

1. Launch EC2 instances using the Amazon ECS-optimized AMI
2. Ensure the instances have the following:
   - IAM role with appropriate permissions for ECS
   - Security groups allowing traffic on your application port (5000)
   - ECS agent installed and configured
   - Sufficient CPU and memory resources

3. Register the EC2 instances with your ECS cluster

### 3. Configure GitHub Secrets

The following secrets need to be configured in your GitHub repository:

- `AWS_IAM_ARN`: ARN of the IAM role with permissions to deploy to ECS
- `AWS_REGION`: AWS region where your ECS cluster is located
- `AWS_ACCOUNT_ID`: Your AWS account ID
- `ECR_REPO_NAME`: Name of your ECR repository
- `CONTAINER_NAME`: Name of the container as defined in your task definition
- `ECS_SERVICE`: Name of your ECS service
- `ECS_CLUSTER`: Name of your ECS cluster

## Local Development

To run the application locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python src/app.py
```

## Docker Build

To build and run the Docker container locally:

```bash
# Build the image
docker build -t python-app .

# Run the container
docker run -p 5000:5000 python-app
