from coinbase.rest import RESTClient
import json
import os
from dotenv import load_dotenv
import http.client

load_dotenv()

api_secret_key = os.environ.get("API_SECRET_KEY")
api_public_key = os.environ.get("API_PUBLIC_KEY")
org_id = os.environ.get("ORG_ID")
base_url = os.environ.get("BASE_URL")


def fetch_public_product_http_client(product_id):
    conn = http.client.HTTPSConnection("api.coinbase.com")
    request_path = f"/api/v3/brokerage/market/products/{product_id}"
    
    headers = {
        "Content-Type": "application/json"
    }

    conn.request("GET", request_path, "", headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

if __name__ == "__main__":
    crypto_pair = "DOT-USD"  
    fetch_public_product_http_client(crypto_pair)
