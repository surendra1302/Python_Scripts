import boto3

def list_ec2_instances(region='ap-south-1'):
    ec2_client = boto3.client('ec2', region_name=region)

    response = ec2_client.describe_instances()

    print(f"Listing EC2 instances in region: {region}\n")
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance.get('InstanceId', 'N/A')
            instance_type = instance.get('InstanceType', 'N/A')
            state = instance.get('State', {}).get('Name', 'N/A')
            public_ip = instance.get('PublicIpAddress', 'N/A')
            private_ip = instance.get('PrivateIpAddress', 'N/A')

            print(f"Instance ID: {instance_id}")
            print(f"Instance Type: {instance_type}")
            print(f"State: {state}")
            print(f"Public IP: {public_ip}")
            print(f"Private IP: {private_ip}")
            print("-" * 60)

if __name__ == "__main__":
    list_ec2_instances(region='ap-south-1')

