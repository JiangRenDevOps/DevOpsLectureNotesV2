# Creating a Three-Tier Architecture in AWS

## Introduction
A three-tier architecture is a software architecture pattern where the application is broken down into three logical tiers: the presentation layer, the business logic layer and the data storage layer. 

This architecture is used in a client-server application such as a web application that has the frontend, the backend and the database. Each of these layers or tiers does a specific task and can be managed independently of each other. 

This is a shift from the monolithic way of building an application where the frontend, the backend and the database are both sitting in one place.

![Alt text](../images/multi-tier/3tier-2.png?raw=true)

## What we got from it?

- **Modularity**: The essence of having a three-tier architecture is to modularize our application such that each part can be managed independently of each other. With modularity, teams can focus on different tiers of the application and changes made as quickly as possible. Also, modularization helps us recover quickly from an unexpected disaster by focusing solely on the faulty part.

- **Scalability**: Each tier of the architecture can scale horizontally to support the traffic and request demand coming to it. This can easily be done by adding more EC2 instances to each tier and load balancing across them. For instance, assuming we have two EC2 instances serving our backend application and each of the EC2 instances is working at 80% CPU utilization, we can easily scale the backend tier by adding more EC2 instances to it so that the load can be distributed. We can also automatically reduce the number of the EC2 instances when the load is less.

- **High Availability**: With the traditional data centre, our application is sitting in one geographical location. If there is an earthquake, flooding or even power outage in that location where our application is hosted, our application will not be available. With AWS, we can design our infrastructure to be highly available by hosting our application in different locations known as the availability zones.

- **Fault Tolerant**: We want our infrastructure to comfortably adapt to any unexpected change both to traffic and fault. This is usually done by adding a redundant system that will account for such a hike in traffic when it does occur. So instead of having two EC2 instances working at 50% each, such that when one instance goes bad, the other instance will be working at 100% capacity until a new instance is brought up by our Auto Scaling Group, we have extra instance making it three instances working at approximately 35% each. This is usually a tradeoff made against the cost of setting up a redundant system.

- **Security**: We want to design an infrastructure that is highly secured and protected from the prying eyes of hackers. As much as possible, we want to avoid exposing our interactions within the application over the internet. This simply means that the application will communicate within themselves with a private IP. The presentation (frontend) tier of the infrastructure will be in a private subnet (the subnet with no public IP assigned to its instances) within the VPC. Users can only reach the frontend through the application load balancer. The backend and the database tier will also be in the private subnet because we do not want to expose them over the internet. We will set up the Bastion host for remote SSH and a NAT gateway for our private subnets to access the internet. The AWS security group helps us limit access to our infrastructure setup.

## Prerequisite
Please ensure you have an AWS account. We shall be making use of the AWS free-tier resources so we do not incur charges while learning.

Note: At the end of this tutorial, you need to stop and delete all the resources such as the EC2 instances, Auto Scaling Group, Elastic Load Balancer etc you set up in case you get charged.

Let's get started!

## Prepare parameters for CFN

We are going to use CloudFormation to create the initial architecture from a dummy app in AWS.

Let us look at it in detail. Refer to `./hands_on/CFN-multi-tier-app.yaml`

Tip: Click View in Designer to check it out.

### Create one VPC and two subnets
- Setup the Virtual Private Cloud (VPC)
    https://console.aws.amazon.com/vpc/home?region=us-east-1#vpcs:sort=desc:VpcId
    
    VPC stands for Virtual Private Cloud (VPC). It is a virtual network where you create and manage your AWS resource in a more secure and scalable manner. Go to the VPC section of the AWS services, and click on the Create VPC button.
    Give your VPC a name and a CIDR block of 10.0.0.0/16
    
    ![Alt text](../images/multi-tier/vpc.png?raw=true)
    
    also, we need to enable public dns domain (so later we can check the instances. see more https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support)
    
    ![Alt text](../images/multi-tier/enable dns.png?raw=true)

- Setup the Internet Gateway

    The Internet Gateway allows communication between the EC2 instances in the VPC and the internet. To create the Internet Gateway, navigate to the Internet Gateways page and then click on Create internet gateway button.
    
    We need to attach our VPC to the internet gateway. To do that:
    
    a. we select the internet gateway
    
    ![Alt text](../images/multi-tier/ig.png?raw=true)
    
    b. Click on the Actions button and then select Attach to VPC.
    
    ![Alt text](../images/multi-tier/attach-vpc.png?raw=true)
    
    c. Select the VPC to attach the internet gateway and click Attach
    
    ![Alt text](../images/multi-tier/attach-vpc2.png?raw=true)

- Create two subnets
    https://console.aws.amazon.com/vpc/home?region=us-east-1#subnets:sort=desc:tag:Name
    
    You can give any names, but both of them are public.
    ![Alt text](../images/multi-tier/public-subnet.png?raw=true)

- Create a public Route Table

    We need to route the traffic to the internet through the internet gateway for our public route table.
    To do that we select the public route table and then choose the Routes tab. The rule should be similar to the one shown below:
    
    ![Alt text](../images/multi-tier/route-table.png?raw=true)
    
    What is VPC and Subnet?
    https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html
    
    What is CIDR?
    Classless inter-domain routing (CIDR) is a set of Internet protocol (IP) standards that is used to create unique identifiers for networks and individual devices. The IP addresses allow particular information packets to be sent to specific computers.
    
    When you create a VPC, you must specify a range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. This is the primary CIDR block for your VPC. 

### Configure user key pair
Make sure you have a user key pair to access your EC2 instance
https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#KeyPairs:sort=keyName

You can create or import one.

### Configure Security Group

- Create Security Group for EC2 instances.

Make sure you have allowed ssh and http as the inbound rule.
![Alt text](../images/multi-tier/ec2-sg.png?raw=true)

### Configure CFN to use parameters.

- Create a stack in AWS CloudFormation
https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/template

use the template in `./hands_on/CFN-multi-tier-app.yaml`

![Alt text](../images/multi-tier/create-cfn.png?raw=true)

- Fill in the parameters required and create the stack

![Alt text](../images/multi-tier/cfn-parameters.png?raw=true)

### Exam what has been created by CFN

- Check the resources in CFN
![Alt text](../images/multi-tier/cfn-resources.png?raw=true)

- Inspect each resource in the console

- Access the LB in the browser.
![Alt text](../images/multi-tier/find-lb.png?raw=true)

  You should be able to see
![Alt text](../images/multi-tier/lb-result.png?raw=true)

- Access the web server in the browser

  Find the public ip from EC2 services.
![Alt text](../images/multi-tier/web-server.png?raw=true)

  You should be able to see
![Alt text](../images/multi-tier/welcom-msg.png?raw=true)

- Access the app server in the browser

  Since we have installed Tomcat in the app server, can you access to
  tomcat server `http://<app instance public ip>:8080`?

- Q: What is the result? Do you know why? Do you know how to access to it?

### Inspect the architecture

- What are some good highlights?
    - LB backed by 2 web-tier EC2 instances running Apache.
    - web-tier EC2 instances are created in different availability zones of the region.
    - Security: 
    
       a. VPC and 2 subnets
       
       b. web-tier EC2 are only accessible via LB, but not exposed publicly.
       
       c. app-tier is not exposed publicly.

- What are some bad highlights?
    - two web servers may not be enough to handle the load if we have more users
    - single point failure in App server
    - App server lives in public subnet
    - No DB layer

## Add Auto Scaling Group in Web Tier
Right now we have 2 instances running, but it is not enough to handle user load. So we need to create ASG to handle the load automatically.

### Create Launch Template
Use new Launch template before creating ASG. 
https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#CreateTemplate:

The good things about Launch Template over Launch Configuration are
1) you don't need to specify those again and again when you spin up a EC2
2) you have version control
    
More on launch template: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html

- Create a Launch template

    ami: use : ami-09d95fab7fff3776c
    
    instance type: t2.micro (free-tier)
    
    key pair name: same as before
    
    ![Alt text](../images/multi-tier/launch-template-settings.png?raw=true)
    
    network: enable public ip and select ec2 private security group
    
    Note: it is only for the convenience of checking at instances in the browser
    
    ![Alt text](../images/multi-tier/network-interface.png?raw=true)

- Update Launch template

    Notice: the instances don't have apache installed and also we want to check its host and availability zone for testing.
    
    We have a way to use user data in EC2. Let us update it.
    ![Alt text](../images/multi-tier/add-user-data.png?raw=true)
    
    Add the following script to user data in Advanced section.
    
    ```bash
    #!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd.service
    systemctl enable httpd.service
    EC2_AVAIL_ZONE=$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)
    echo "<h1>Hello World From Multi-Tier Sample App at at $(hostname -f) in AZ $EC2_AVAIL_ZONE </h1>" > /var/www/html/index.html
    ```
    
    ![Alt text](../images/multi-tier/add-user-script.png?raw=true)
    
    Set the new template as the default
    ![Alt text](../images/multi-tier/add-user-template.png?raw=true)

### Create ASG
- Create ASG 
    https://console.aws.amazon.com/ec2autoscaling/home?region=us-east-1#/create
    
    Select the Launch Template just created
    ![Alt text](../images/multi-tier/asg-template.png?raw=true)
    
    Select VPC, subnets, healthcheck as ec2, target group
    ![Alt text](../images/multi-tier/It-subnets.png?raw=true)
    
    Set the intances between 1 and 3 to experiment
    ![Alt text](../images/multi-tier/asg-scale.png?raw=true)
    
    Review and make sure everything looks correct
    ![Alt text](../images/multi-tier/asg-review.png?raw=true)

- Inspect the instances created by ASG
    ![Alt text](../images/multi-tier/asg-check-instance.png?raw=true)
    
    You should be able to see
    ![Alt text](../images/multi-tier/It-result.png?raw=true)

- Inspect all instances from the target group directed from LB

![Alt text](../images/multi-tier/lb-all-instances.png?raw=true)

- Change the desired to 2 in ASG and inspect what's going on

![Alt text](../images/multi-tier/asg-desired.png?raw=true)

- Remove the two instance created from the CloudFormation template

    since we have ASG to control the instance, we can remove the ones created from the CFN template


### Add ASG policy

#### Different policies:

• Target Tracking Scaling

    • Most simple and easy to set-up
    • Example: I want the average ASG CPU to stay at around 40%
• Simple / Step Scaling
    
    • When a CloudWatch alarm is triggered (example CPU > 70%), then add 2 units 
    • When a CloudWatch alarm is triggered (example CPU < 30%), then remove 1
• Scheduled Actions

    • Anticipate a scaling based on known usage patterns
    • Example: increase the min capacity to 10 at 5 pm on Fridays

https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html#as-scaling-types

#### ASG Brain Dump
• Scaling policies can be on CPU, Network... and can even be on custom metrics or based on a schedule (if you know your visitors patterns)

• ASGs use Launch configurations or Launch Templates (newer)

• To update an ASG, you must provide a new launch configuration / launch template

• IAM roles attached to an ASG will get assigned to EC2 instances

• ASG are free.You pay for the underlying resources being launched

• Having instances under an ASG means that if they get terminated for whatever reason, the ASG will automatically create new ones as a replacement. Extra safety!

• ASG can terminate instances marked as unhealthy by an LB (and hence replace them)

Note: The following can be the homework if we don't have time.

## Recreate on App Tier

### Create 2 private subnets

A subnet can be public or private. EC2 instances within a public subnet have public IPs and can directly access the internet while those in the private subnet does not have public IPs and can only access the internet through a NAT gateway.

### Create a private route table

private route table will define which subnet goes through the NAT gateway (ie private subnet).

Associate the private route table with the private subnets above

### Create a NAT gateway

**Warning: NAT is Not included in Free Tier!**

The NAT gateway enables the EC2 instances in the private subnet to access the internet. The NAT Gateway is an AWS managed service for the NAT instance. To create the NAT gateway, navigate to the NAT Gateways page, and then click on the Create NAT Gateway.

Please ensure that you know the Subnet ID for a public subnet created before. This will be needed when creating the NAT gateway.

Now that we have the NAT gateway, we are going to edit the private route table to make use of the NAT gateway to access the internet.

### Create ALB in App Tier
https://console.aws.amazon.com/ec2/v2/home?region=us-east-1#LoadBalancers:sort=loadBalancerName

- select the two private subnet.
- we only open the port that the backend runs on (eg: port 3000) and the make such port only open to the security group of the frontend. This will allow only the frontend to have access to that port within our architecture.

Reference: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-register-lbs-with-asg.html

Note: 
- ALB relies on the target group to find which instances to redirect
- It takes a few mins to create ALB.

### Create ASG in App Tier
Can you please add ASG in the App Tier, similarly like what we did in Web Tier?

### Bastion Host

The bastion host is just an EC2 instance that sits in the public subnet. 

The best practice is to only allow SSH to this instance from your trusted IP. 
- Config the security group for the bastion host 
To create a bastion host, navigate to the EC2 instance page and create an EC2 instance in the public subnet within our VPC. Also, ensure that it has public IP.
- Config the security group for instances in App Tier by only selecting bastion host ip

## Create DB Tier

### Create RDS in DB Tier
https://console.aws.amazon.com/rds/home?region=us-east-1#launch-dbinstance:gdb=false;s3-import=false

Here are some interesting settings:
- Multi-AZ deployment
- Storage autoscaling
- Public Accessibility
- Security Group
    Create a security group with only access from App in our case. e.g.
    ![Alt text](../images/multi-tier/db-sg.png?raw=true)

See more:

https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html

https://medium.com/@chamikakasun/an-aws-rds-db-instance-in-a-vpc-accessed-by-an-aws-ec2-instance-in-the-same-vpc-befa659b3dd8

## Other References
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html#instance-metadata-ex-6

https://stackoverflow.com/questions/26706683/ec2-t2-micro-instance-has-no-public-dns

What is AZ and Region?
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html