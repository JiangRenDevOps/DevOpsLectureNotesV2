# Description
This is the handson to how to automate the creation of an AWS S3 Bucket, which we will use to deploy a static website using the AWS SDK for Python also known as the Boto3 library. 

# Introduction
- Boto3 is the AWS SDK for Python, which provides Object-based APIs and low-level direct access to AWS services like EC2. 
- AWS CLI is a command line tool written in Python that introduces efficient use cases to manage AWS services with a set of very simple commands. 

# Install AWS CLI and Python Boto3 Library
```python
pip install awscli boto3
```
# Create a User and get AWS Access ID and Secret Key
Now that we've installed the AWS CLI and Boto3, its time to create your user credentials on the AWS console, so that AWS services can be access programmatically. Follow these steps to create your user credentials:

# Configure AWS Credentials Locally
After creating the user and obtaining the credentials (Access ID and Secret key), we can now configure our Python scripting environment with this credential in order to manage EC2. 

Use the AWS CI tool to configure these credentials by running the following command from a Bash terminal: 

```bash
aws configure
```
It will prompt you to provide the Access Key ID, Secret Key, Default AWS region, and output format. Once those are provided, credentials are saved in a local file at path ~/.aws/credentials and other configurations like region are stored in ~/.aws/config file as demonstrated in the following example.

Now that we've configured our credentials, let's test if these credentials work well with AWS CLI tools. To do that, run the following command from a Bash shell: 
```bash
aws s3 ls
```

This should give you the available S3 if you have.

# Configure AWS Credentials Locally

To list all Buckets  users in your console using Python, simply import the boto3 library in Python and then use the ‘list_buckets()’ method of the S3 client, then iterate through all the buckets available to list the property ‘Name’ like in the following image.

```python
import boto3
import json


s3 = boto3.client('s3')

def list_buckets():
    # List of existing buckets
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        print('BucketName: {}'.format(bucket['Name']))

if __name__ == "__main__":
    list_buckets()        
```
But to host a static website, we need a publicly available bucket that is open to everyone on the internet. So let's create a new bucket. 

# Creating a New AWS S3 Bucket and Assigning Bucket Policy
First thing's first, import the ‘boto3’ library in Python, then call the AWS S3 client. Now use the ‘create_bucket()’ method on the client and provide a ‘Bucket Name’, which is ‘michaelsu-static-website’ in our example. 
This will create a new AWS S3 bucket and you can also verify that by listing the names of existing buckets again as described in the previous example.

But since this website should be publically open, we need assign a ‘bucket policy’ to this ‘bucket: prateek-static-website’ with read-only permissions for any anonymous user. 
So now I will create the bucket policy in JSON format and assign ‘"Action":["s3:GetObject"]’ permission to only grant the ‘read-only’ rights to any users using the wildcard in ‘"Principal": "*"’. Then using the ‘put_bucket_policy()’ method of S3 client we will assign this policy to the bucket.

```python
# bucket_name needs to be unique
bucket_name = 'michaelsu-static-website'

def create_bucket():
    # Create bucket
    s3.create_bucket(Bucket=bucket_name)


def update_bucket_policy():
    # Define public policy
    bucket_policy = {
        'Version': '2012-10-17',
        'Statement': [{
            'Sid': 'AddPerm',
            'Effect': 'Allow',
            'Principal': '*',
            'Action': ['s3:GetObject'],
            'Resource': "arn:aws:s3:::%s/*" % bucket_name
        }]
    }

    bucket_policy = json.dumps(bucket_policy)

    # update policy to the bucket
    s3.put_bucket_policy(Bucket=bucket_name, Policy=bucket_policy)
```

# Enable Static Website Hosting on AWS S3 Bucket
You now need to explicitly enable the AWS S3 Bucket to host static websites and provide the website configurations like the Index and Error HTML page.  This can be achieved by calling the ‘put_bucket_website()’ method of S3 client and passing the ‘bucket name’ and Website configuration in a hash table that stores the name of the files Index and Error files, like ‘index.html’ and ‘error.html’ respectively.

```python
def enable_htmls():
    # Enable S3 to host static website
    s3.put_bucket_website(
        Bucket=bucket_name,
        WebsiteConfiguration={
            'ErrorDocument': {'Key': 'error.html'},
            'IndexDocument': {'Suffix': 'index.html'},
        }
    )
```

# Uploading HTML Documents for the Static Website
Now I will simply create two HTML files one for the main Static website page also known as the ‘index.html’

```html
<html>
 <body>
 <h1>Hello World!</h1>
 </body>
 </html>
```

And an error page that will appear when something goes wrong on our static website, which is referred as ‘error.html’.
```html
<html>
 <body>
 <h1>Oh. Something bad happened!</h1>
 </body>
 </html>
```

Once we have these two HTML files prepared locally, we can utilize the ‘put_object()’ method of S3 client and upload these to our target AWS S3 bucket.
```python
def upload_htmls():
    # Upload htmls to S3
    filename = ['index.html', 'error.html']
    for file in filename:
        data = open(file, "rb")
        s3.put_object(Body=data,
                      Bucket=bucket_name,
                      Key=file,
                      ContentType='text/html')
```

Now, if we browse the URL of our static website in the following syntax through a web browser.

https://{Name-Of-Bucket}.s3-website-{Region}.amazonaws.com

In our example, it is http://michaelsu-static-website.s3-website-us-east-1.amazonaws.com
![Alt text](images/s3_host.png?raw=true)
