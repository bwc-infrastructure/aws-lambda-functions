#!/usr/bin/env python3
import boto3



# Create the CloudFormation stack
def lambda_handler(event, context):
    # Set the AWS region and create a CloudFormation client
    region_name = 'us-east-1'
    cf_client = boto3.client('cloudformation', region_name=region_name)

    # Set the stack name and CloudFormation template file path
    stack_name = 'my-stack'
    template_path = 'path/to/cloudformation/template.yaml'
    cf_client.create_stack(
        StackName=stack_name,
        TemplateBody="s3://path-to-cloudformation",
        Capabilities=['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM'],
        Parameters=[
            {
                'ParameterKey': 'InstanceType',
                'ParameterValue': 't2.micro'
            },
            {
                'ParameterKey': 'KeyName',
                'ParameterValue': 'my-keypair'
            }
        ],
        TimeoutInMinutes=30,
        OnFailure='DELETE',
        Tags=[
            {
                'Key': 'Environment',
                'Value': 'dev'
            },
            {
                'Key': 'Owner',
                'Value': 'John Doe'
            }
        ]
    )
