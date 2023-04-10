#!/bin/bash



# Check if the bucket exists
if aws s3 ls "s3://${BUCKET_NAME}" 2>&1 | grep -q 'NoSuchBucket'; then
    echo "Bucket does not exist. Creating new bucket..."
    # Create the bucket with default options
    aws s3 mb "s3://${BUCKET_NAME}"
else
    echo "Bucket already exists"
fi
