import boto3, base64, json

def lambda_handler(event, context):
    body = event.get("body")
    if isinstance(body, str):
        body = json.loads(body or "{}")
    body = body or {}

    bucket = body.get("bucket")
    key = body.get("key")
    content_b64 = body.get("content_base64")
    if not bucket or not key or not content_b64:
        return {"statusCode": 400, "body": json.dumps({"error": "Faltan 'bucket', 'key' y/o 'content_base64'"})}

    data = base64.b64decode(content_b64)
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket, Key=key, Body=data)
    return {"statusCode": 200, "body": json.dumps({"message": "Objeto subido", "bucket": bucket, "key": key, "size": len(data)})}
