import boto3, json

def lambda_handler(event, context):
    body = event.get("body")
    if isinstance(body, str):
        body = json.loads(body or "{}")
    body = body or {}

    bucket = body.get("bucket")
    prefix = body.get("prefix")  # ej: "imagenes/"
    if not bucket or not prefix:
        return {"statusCode": 400, "body": json.dumps({"error": "Faltan 'bucket' y/o 'prefix'"})}

    if not prefix.endswith("/"):
        prefix += "/"
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket, Key=prefix)
    return {"statusCode": 200, "body": json.dumps({"message": "Prefijo creado", "bucket": bucket, "prefix": prefix})}
