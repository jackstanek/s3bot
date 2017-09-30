"""Higher-level interface using s3bot."""

import os

import boto3

import s3bot

def read_keys(keyfile):
    """Get access keys from a key file."""
    with open(keyfile, "r") as keyfileobj:
        return tuple(key.strip() for key in keyfileobj.readlines())

class NoSuchS3ObjectError(Exception):
    """Denotes that an object does not exist"""
    pass

class NoSuchS3BucketError(Exception):
    """Denotes that a bucket does not exist"""

class S3Wrapper:
    """Connection to interface with MSI's S3 instance."""

    keyfile = "test.txt" #os.path.join(s3bot.SHARED_BASE, ".s3keys")
    delimiter = "/"
    default_bucket = "mccuelab"

    def __init__(self):
        access_key, secret_key = read_keys(S3Wrapper.keyfile)

        kwargs = {
            "endpoint_url": s3bot.S3_BASE_URL,
            "aws_access_key_id": access_key,
            "aws_secret_access_key": secret_key
        }

        self.conn = boto3.client("s3", **kwargs)
        self.buckets = tuple(b["Name"] for b in self.conn.list_buckets()["Buckets"])


    def bucket_contents(self, prefix, bucket_name=default_bucket):
        """Generator to return bucket contents matching the given prefix"""
        if bucket_name in self.buckets:
            resp = self.conn.list_objects(Bucket=bucket_name,
                                          Delimiter=S3Wrapper.delimiter,
                                          Prefix=prefix)
            if "CommonPrefixes" in resp:
                prefixes = [item["Prefix"] for item in resp["CommonPrefixes"]]
                for pfx in prefixes:
                    yield pfx
            elif "Contents" in resp:
                keys = [item["Key"] for item in resp["Contents"]]
                for key in keys:
                    yield key
            else:
                raise NoSuchS3ObjectError()

        else:
            raise NoSuchS3BucketError()
