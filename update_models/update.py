import boto3
import os
from datetime import datetime
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('MODELS_TABLE')
table = dynamodb.Table(table_name)

def main(event, context):
    """
    This cron job updates models data in DynamoDB.
    """
    print("Updating models...")

    # For now: static data. Later → scrape OpenAI / Bedrock / Anthropic.
    models = [
        {
            "provider_model": "OpenAI#gpt-4o-mini",
            "provider": "OpenAI",
            "model": "gpt-4o-mini",
            "price_prompt": Decimal("0.0005"),
            "price_completion": Decimal("0.0015"),
            "context_length": Decimal("128000"),
            "quality_score": Decimal("7"),
            "date_updated": datetime.now().isoformat()
        },
        {
            "provider_model": "OpenAI#gpt-4o",
            "provider": "OpenAI",
            "model": "gpt-4o",
            "price_prompt": Decimal("0.01"),
            "price_completion": Decimal("0.03"),
            "context_length": Decimal("128000"),
            "quality_score": Decimal("9"),
            "date_updated": datetime.now().isoformat()
        }
    ]

    # Upsert each item
    for item in models:
        table.put_item(Item=item)
        print(f"Updated {item['provider_model']}")

    print("Update complete.")

    return {"status": "success", "models_updated": len(models)}