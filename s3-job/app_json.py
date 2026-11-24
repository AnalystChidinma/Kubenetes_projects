import json
import os
import random
from datetime import datetime, timedelta

import boto3

PRODUCTS = ["laptop", "phone", "headphones", "smartwatch", "tablet"]
CITIES = ["Lagos", "Abuja", "Ibadan", "Port Harcourt", "Kano"]


def generate_orders(num_rows):
    """Build a list of fake order records."""
    orders = []
    for order_id in range(1, num_rows + 1):
        orders.append({
            "order_id": order_id,
            "customer_id": random.randint(1000, 1999),
            "product": random.choice(PRODUCTS),
            "quantity": random.randint(1, 5),
            "unit_price": round(random.uniform(5000, 500000), 2),
            "city": random.choice(CITIES),
            "order_date": (datetime.now() - timedelta(days=random.randint(0, 30))).date().isoformat(),
        })
    return orders


def upload_to_s3(orders, bucket, key):
    """Upload the records to S3 as a JSON file."""
    s3 = boto3.client("s3")
    s3.put_object(Bucket=bucket, Key=key, Body=json.dumps(orders))


if __name__ == "__main__":

    num_rows = int(os.environ.get("NUM_ROWS", "100"))
    bucket = os.environ["BUCKET_NAME"]
    prefix = os.environ.get("S3_PREFIX", "orders")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    key = f"{prefix}/orders_{timestamp}.json"

    orders = generate_orders(num_rows)
    print(f"Generated {num_rows} rows")

    print(f"Uploading to s3://{bucket}/{key}")
    upload_to_s3(orders, bucket, key)
    print("Upload complete")