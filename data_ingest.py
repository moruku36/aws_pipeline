
import csv
import json
import time
from datetime import datetime
import boto3  # AWS SDK for Python

# Initialize Kinesis client
kinesis = boto3.client('kinesis', region_name='us-east-1')

def read_csv_and_send_to_kinesis(csv_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            row['timestamp'] = datetime.utcnow().isoformat()  # Add timestamp
            payload = json.dumps(row)
            
            # Send data to Kinesis Stream
            kinesis.put_record(
                StreamName='MyKinesisStream',
                Data=payload,
                PartitionKey='partition_key'
            )
            time.sleep(0.1)  # Simulate sending at least 10 records per second

if __name__ == "__main__":
    read_csv_and_send_to_kinesis('path/to/your/csv/file.csv')
