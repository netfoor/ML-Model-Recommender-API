import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('MODELS_TABLE')
table = dynamodb.Table(table_name)

def get_all_models(provider=None):
    """
    Get all models, or filter by provider (very basic; real use: use a GSI)
    """
    response = table.scan()
    items = response.get('Items', [])

    if provider:
        items = [item for item in items if item.get('provider') == provider]

    return items
