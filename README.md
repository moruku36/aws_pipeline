# aws_pipeline

# AWS Real-Time Data Ingest Pipeline

This repository contains the code and configuration files for setting up a real-time data ingest pipeline using AWS services.

## Overview

The pipeline reads data from a CSV file (`recommended-fishing-rivers-and-streams-1.csv`) and streams it into an AWS Kinesis Stream. It also includes a Terraform configuration for setting up the Kinesis Stream and bash scripts for building, testing, and deploying the pipeline.

## Files

- `data_ingest.py`: Python script for reading data from the CSV file and sending it to the Kinesis Stream.
- `unit_test.py`: Python script for running unit tests on `data_ingest.py`.
- `main.tf`: Terraform configuration file for setting up AWS resources (Kinesis Stream).
- `build.sh`: Bash script for building the application.
- `unit_test.sh`: Bash script for running unit tests.
- `deploy.sh`: Bash script for deploying the AWS infrastructure using Terraform.
- `stream.sh`: Bash script for running `data_ingest.py` to start the data streaming.

## Setup

1. Make sure you have AWS CLI and Terraform installed.
2. Run `build.sh` to build the application.
3. Run `unit_test.sh` to execute unit tests.
4. Run `deploy.sh` to deploy the AWS infrastructure.
5. Run `stream.sh` to start the data streaming.



