import boto3
client = boto3.client("ec2", region_name="us-east-1")
client.stop_instances(InstanceIds=['i-0d880c98d421a1298'])