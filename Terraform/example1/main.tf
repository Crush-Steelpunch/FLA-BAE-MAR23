terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}


provider "aws" {
  region = "eu-west-2"
}

resource "aws_instance" "this" {
  #ami                    = "ami-09744628bed84e434"
  ami                    = var.awsimageid
  key_name               = "fla-may15"
  instance_type          = "t2.micro"
  vpc_security_group_ids = [aws_security_group.allow_ssh.id, "sg-0b1e75c9741f11704"]
  tags = {
    Name = "Terraform Instance"
  }
}

resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh"
  description = "Allow ssh inbound traffic"
  vpc_id      = "vpc-0f03c543cd14b23ac"

  ingress {
    description      = "SSH from VPC"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name        = "allow_tls"
    Project     = "Project1"
    Environment = "Prod"
  }
}


output "PublicIP" {
  value = aws_instance.this.public_ip
}
output "InstanceState" {
  value = aws_instance.this.instance_state
}

module "Submodue1" {
  source = "./example-module"
  
}

variable awsimageid {
  type = string
#  default = "ami-028a5cd4ffd2ee495"
}