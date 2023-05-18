resource "aws_s3_bucket" "example" {
  bucket = var.mys3bucketname

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}