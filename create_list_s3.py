import boto3
from botocore.exceptions import ClientError

# Initialize the S3 client
s3 = boto3.client('s3', region_name='ap-south-1')  # Replace with your region

# Create the bucket
try:
    response = s3.create_bucket(
        Bucket='surendra13-mock-test',
        CreateBucketConfiguration={
            'LocationConstraint': 'ap-south-1'  # Replace with your desired region
        }
    )
    print(f"Bucket {'surendra13-mock-test'} created successfully!")

except ClientError as e:
    print(f"Error creating bucket: {e}")

# List the buckets
try:
    response = s3.list_buckets()
    print("\nExisting S3 Buckets:")
    for bucket in response['Buckets']:
        print(f"- {bucket['Name']}")

except ClientError as e:
    print(f"Error listing buckets: {e}")

