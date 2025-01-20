import boto3
from botocore.exceptions import NoCredentialsError

def test_credentials():
    try:
        # Create an S3 client using the AWS credentials
        s3_client = boto3.client('s3')
        # Try to list buckets to check if the credentials are valid
        s3_client.list_buckets()
    except NoCredentialsError:
        raise AssertionError("AWS credentials are not provided or are incorrect.")
    except Exception as e:
        raise AssertionError(f"An error occurred while accessing AWS: {str(e)}")
