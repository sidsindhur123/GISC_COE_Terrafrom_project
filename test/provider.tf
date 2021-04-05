provider "aws" {
    profile = "default"
    shared_credentials_file = "~/.aws/credentials"
    region = "${var.region}"
}