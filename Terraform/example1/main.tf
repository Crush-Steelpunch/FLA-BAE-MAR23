terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
    }
  }
}


provider "aws" {
  region = "eu-west-2"
}

resource "aws_instance" "this" {
  ami                     = "ami-09744628bed84e434"
  key_name                = "fla-may15"
  instance_type           = "t2.micro"
  vpc_security_group_ids  =  ["sg-0851886f344803422","sg-0b1e75c9741f11704" ]
}