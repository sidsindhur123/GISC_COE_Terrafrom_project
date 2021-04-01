

resource "aws_vpc" "vpc" {
  cidr_block       = var.cidr_block
  instance_tenancy = "default"

  tags = {
    Name = "${var.env}_vpc"
  }
}


output "vpc_id" {
  value = aws_vpc.vpc.id
}
