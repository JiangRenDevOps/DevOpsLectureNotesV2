terraform {
  backend "s3" {
    encrypt = true
    bucket = "terraform-remote-state-storage-s3-msu"
    region = "us-east-1"
    key = "./terraform.tfstate"
    profile = "default"

    # Replace this with your DynamoDB table name!
    dynamodb_table = "terraform-state-lock-dynamodb"
  }
}