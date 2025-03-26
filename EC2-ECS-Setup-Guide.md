# Setting Up EC2 Instances for Amazon ECS

This guide provides instructions for setting up EC2 instances to be used with Amazon ECS (Elastic Container Service).

## Prerequisites

- AWS account with appropriate permissions
- Basic knowledge of AWS services (EC2, ECS, IAM)
- Understanding of networking concepts

## Step 1: Create an ECS Cluster with EC2 Launch Type

1. Navigate to the Amazon ECS console
2. Click "Create Cluster"
3. Select "EC2 Linux + Networking"
4. Configure your cluster:
   - **Cluster name**: Enter a name for your cluster (e.g., python-app-cluster)
   - **EC2 instance type**: Choose an appropriate instance type (e.g., t2.micro, t2.small)
   - **Number of instances**: Specify how many EC2 instances to launch
   - **EC2 AMI ID**: Use the Amazon ECS-optimized AMI (default)
   - **EBS storage**: Configure storage as needed
   - **Key pair**: Select an existing key pair or create a new one
   - **VPC and subnets**: Select your VPC and subnets
   - **Security group**: Create a new security group or select an existing one
   - **IAM role**: Use the default ecsInstanceRole or create a custom role

5. Click "Create"

## Step 2: Configure Security Groups

Ensure your security group allows:
- Inbound traffic on port 5000 (for your application)
- Outbound traffic as needed
- SSH access (port 22) for administration

## Step 3: Verify EC2 Instances in Your Cluster

1. Once the cluster is created, go to the ECS Clusters dashboard
2. Select your cluster
3. Click on the "ECS Instances" tab
4. Verify that your EC2 instances are registered and active

## Step 4: Create a Task Definition

1. In the ECS console, go to "Task Definitions"
2. Click "Create new Task Definition"
3. Select "EC2" as the launch type
4. Configure your task definition:
   - **Task Definition Name**: Enter a name (e.g., python-app)
   - **Task Role**: Select an appropriate IAM role
   - **Network Mode**: Choose "bridge" for EC2 instances
   - **Task execution role**: Select the ecsTaskExecutionRole
   - **Task memory**: Specify the memory limit (e.g., 512 MB)
   - **Task CPU**: Specify the CPU limit (e.g., 256)

5. Add a container:
   - **Container name**: Enter a name (e.g., python-app)
   - **Image**: Enter your ECR image URI
   - **Memory Limits**: Set soft and hard limits
   - **Port mappings**: Map container port 5000 to host port 0 (dynamic port mapping)
   - **Environment variables**: Add as needed
   - **Log configuration**: Configure CloudWatch logs

6. Click "Create"

## Step 5: Create an ECS Service

1. In your ECS cluster, click "Create"
2. Configure your service:
   - **Launch type**: EC2
   - **Task Definition**: Select your task definition
   - **Service name**: Enter a name (e.g., python-app-service)
   - **Service type**: REPLICA
   - **Number of tasks**: Specify how many tasks to run
   - **Deployment type**: Rolling update
   - **Placement Templates**: AZ Balanced Spread

3. Configure networking:
   - **Load balancer type**: Application Load Balancer (if needed)
   - **Service discovery**: Configure if needed

4. Configure Auto Scaling (optional)
5. Click "Create Service"

## Step 6: Monitor Your Service

1. In your ECS cluster, select your service
2. Monitor the "Tasks" tab to ensure tasks are running
3. Check the "Events" tab for any issues
4. Use CloudWatch logs to view application logs

## Troubleshooting

- **EC2 instances not joining cluster**: Check IAM roles and ECS agent configuration
- **Tasks not starting**: Check resource constraints and container configuration
- **Application not accessible**: Verify security groups and port mappings
- **ECS agent issues**: SSH into the instance and check `/var/log/ecs/ecs-agent.log`

## Additional Resources

- [Amazon ECS Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
- [ECS-Optimized AMI](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html)
- [Task Definition Parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html)
- [Amazon ECS Service Parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service_definition_parameters.html)
