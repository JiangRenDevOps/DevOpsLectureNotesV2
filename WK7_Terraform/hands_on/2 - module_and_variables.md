# Module
A module is a container for multiple resources that are used together.

Every Terraform configuration has at least one module, known as its root module, which consists of the resources defined in the .tf files in the main working directory.

A module can call other modules, which lets you include the child module's resources into the configuration in a concise way. Modules can also be called multiple times, either within the same configuration or in separate configurations, allowing resource configurations to be packaged and re-used.

Modules
- subdirctories with self-contained terraform code
- may be sourced from Git, etc.
- use variables and outputs to pass data

# Variables
Variables - Input variables serve as parameters for a Terraform module, allowing aspects of the module to be customized without altering the module's own source code, and allowing modules to be shared between different configurations.

# Version Control
Let us change the main.js to print `Hello World` and upload to s3 v1.0.1 folder

```
$ cd example
$ zip ../example.zip main.js
updating: main.js (deflated 33%)
$ cd ..
$ aws s3 cp example.zip s3://terraform-serverless-msu/v1.0.1/example.zip
```

Create variables.tf in `./staging/services/backend_app` and Add the following:
```
variable "app_version" {
}
```

Go to lambda.tf and change the `s3_key` in `aws_lambda_function` to
```
resource "aws_lambda_function" "example" {
  function_name = "ServerlessExample"

  # The bucket name as created earlier with "aws s3api create-bucket"
  s3_bucket = "terraform-serverless-example"
  s3_key    = "v${var.app_version}/example.zip"
  # (leave the remainder unchanged)
}
```

The terraform apply command now requires a version number to be provided:
```
terraform apply -var="app_version=1.0.1"
```

Note: If you don't specify a version, terraform will ask you.

After the change has been applied, visit again the test URL and you should see the updated greeting message.

###Rollback

```
terraform apply -var="app_version=1.0.0"
```

###Destroy

```
terraform destroy -var="app_version=1.0.0"
```

# Rearrange folders

A typical project layout would look like this
```
staging
  └ vpc
  └ services
      └ frontend-app
      └ backend-app
          └ main.tf
          └ outputs.tf
          └ variables.tf
  └ data-storage
      └ mysql
      └ redis
prod
  └ vpc
  └ services
      └ frontend-app
      └ backend-app
  └ data-storage
      └ mysql
      └ redis
mgmt
  └ vpc
  └ services
      └ bastion-host
      └ jenkins
global
  └ iam
  └ s3
```
Let us rearrange our project like this
```
staging
  └ services
      └ backend-app
          └ main.tf
          └ lambda.tf
          └ api_gateway.tf
          └ output.tf
          └ variables.tf
main.tf
output.tf
variables.tf
```

- Create empty outputs.tf in `backend-app` folder
- Copy the output from lambda.tf to output.tf

```
output "base_url" {
  value = aws_api_gateway_deployment.example.invoke_url
}
```
- Create three empty files under `WK7_Terraform` directory
```
main.tf
output.tf
variables.tf
```

Let us define the module that we would like to use 

Add below into main.tf under `WK7_Terraform` directory
```
module "myApp" {
  source = "./staging/services/backend_app"
  app_version = var.app_version
}
```

Then we need to go to `WK7_Terraform` directory in terminal, and run `terraform init`

if you run terraform apply now, you will see errors that output and variables are not defined.
 
let us fill in the output.tf and variables.tf in the main path

```
output "base_url" {
  value = module.myApp.base_url
}
```

```
variable "app_version" {
}
```

and in the backend_app, the output.tf and variables.tf are defined like this

```
output "base_url" {
  value = aws_api_gateway_deployment.example.invoke_url
}
```

```
variable "app_version" {
}
```

Without these two files, the upper layer output.tf and variables.tf cannot parse correctly

Now run `terraform apply` for the version 1.0.0