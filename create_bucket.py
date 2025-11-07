import boto3, json

def lambda_handler(event, context):
    body = event.get("body")
    if isinstance(body, str):
        body = json.loads(body or "{}")
    body = body or {}

    bucket = body.get("bucket")
    if not bucket:
        return {"statusCode": 400, "body": json.dumps({"error": "Falta 'bucket'"})}

    s3 = boto3.client("s3")
    # En us-east-1 no es necesario CreateBucketConfiguration
    s3.create_bucket(Bucket=bucket)
    return {"statusCode": 200, "body": json.dumps({"message": "Bucket creado", "bucket": bucket})}
