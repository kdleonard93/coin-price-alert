# from coinbase.rest import RESTClient
import json
import os
from dotenv import load_dotenv
from twilio.rest import Client 
import requests

load_dotenv()

API_SECRET_KEY = os.environ.get("API_SECRET_KEY")
API_PUBLIC_KEY = os.environ.get("API_PUBLIC_KEY")
ORG_ID = os.environ.get("ORG_ID")
BASE_URL = os.environ.get("BASE_URL")
TWILIO_API = os.environ.get("TWILIO_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID_KEY")



def fetch_public_product_http_client(product_id):
    url = f"https://{BASE_URL}/api/v3/brokerage/market/products/{product_id}"
    
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        dot_data = response.json()
        dot_price = round(float(dot_data["price"]), 2)
        print(dot_price)
        
        buy_dot = dot_price < 8.70
        
        client = Client(TWILIO_SID, TWILIO_API)
        message = client.messages.create(
            body="Buy some DOT ma boi!!!" if buy_dot else "HODL like vice grips!",
            from_="+18885998708",
            to="+16302012552"
        )
        print(message.status)
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    crypto_pair = "DOT-USD"  
    fetch_public_product_http_client(crypto_pair)
