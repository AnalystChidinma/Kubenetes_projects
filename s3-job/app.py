import csv
import os
import random
from datetime import datetime, timedelta

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

def write_csv(orders, file_path):
    """Save the records to a CSV file."""
    with open(file_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=orders[0].keys())
        writer.writeheader()
        writer.writerows(orders)

if __name__ == "__main__":
    num_rows = int(os.environ.get("NUM_ROWS", "100"))
    file_path = "/tmp/orders.csv"

    orders = generate_orders(num_rows)
    write_csv(orders, file_path)
    print(f"Generated {num_rows} rows at {file_path}")