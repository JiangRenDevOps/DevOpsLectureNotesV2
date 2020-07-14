resource "aws_s3_bucket" "terraform-remote-state-storage-s3-msu" {
  bucket = "terraform-remote-state-storage-s3-msu"

  versioning {
    enabled = true
  }

}

resource "aws_dynamodb_table" "dynamodb-terraform-state-lock" {
  name         = "terraform-state-lock-dynamodb"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"
  attribute {
    name = "LockID"
    type = "S"
  }
}