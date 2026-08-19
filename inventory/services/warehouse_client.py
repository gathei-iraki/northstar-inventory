import requests


WAREHOUSE_URL = (
    "http://127.0.0.1:8000/api/warehouse/products/"
)


def fetch_inventory():
    response = requests.get(
        WAREHOUSE_URL,
        timeout=10,
    )

    response.raise_for_status()

    return response.json()["products"]