import boto3
ec2 = boto3.client('ec2')
def stop_instance(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f"stopped instances: {instance_id}")
stop_instance('i-01400b3ac694b88c5')
