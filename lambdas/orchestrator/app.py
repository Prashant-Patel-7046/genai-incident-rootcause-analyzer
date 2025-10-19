def handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method", "GET")
    path = event.get("requestContext", {}).get("http", {}).get("path", "/")
    if path == "/health":
        return {"statusCode": 200, "headers": {"content-type": "application/json"}, "body": '{"status":"ok"}'}
    return {
        "statusCode": 200,
        "headers": {"content-type": "application/json"},
        "body": '{"message":"analyze stub - replace with Bedrock + Athena soon"}'
    }
