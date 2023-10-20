import boto3
import json

def lambda_handler(event, context):
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2')

    # Initialize the SNS client
    sns_client = boto3.client('sns')

    # Specify the SNS topic ARN where you want to send alerts
    sns_topic_arn = 'arn:aws:sns:ap-south-1:295397358094:EC2DiskSpaceAlert'

    # Get a list of EC2 instances
    instances = ec2_client.describe_instances()

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']

            # Check disk space utilization for the instance
            utilization = check_disk_space(instance_id)

            if utilization > 85:
                # Disk space exceeds 85%, send an alert to SNS
                message = f"Disk space utilization for EC2 instance {instance_id} exceeds 85%."
                sns_client.publish(
                    TopicArn=sns_topic_arn,
                    Message=message,
                    Subject="Disk Space Alert"
                )

def check_disk_space(instance_id):
    pass
