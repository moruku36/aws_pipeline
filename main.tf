
provider "aws" {
  region = "us-east-1"
}

resource "aws_kinesis_stream" "my_stream" {
  name             = "MyKinesisStream"
  shard_count      = 1
  retention_period = 24
}
