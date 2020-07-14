module "myApp" {
  source = "./staging/services/backend_app"
  app_version = var.app_version
}

provider "aws" {
  region                  = "us-east-1"
  shared_credentials_file = "/Users/msu/.aws/credentials"
  profile                 = "default"
}