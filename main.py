# from coinbase.rest import RESTClient
import json
import os
from dotenv import load_dotenv
import http.client
from twilio.rest import Client 

load_dotenv()

API_SECRET_KEY = os.environ.get("API_SECRET_KEY")
API_PUBLIC_KEY = os.environ.get("API_PUBLIC_KEY")
ORG_ID = os.environ.get("ORG_ID")
BASE_URL = os.environ.get("BASE_URL")
TWILIO_API = os.environ.get("TWILIO_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID_KEY")


def fetch_public_product_http_client(product_id):
    conn = http.client.HTTPSConnection(BASE_URL)
    request_path = f"/api/v3/brokerage/market/products/{product_id}"
    
    headers = {
        "Content-Type": "application/json"
    }

    conn.request("GET", request_path, "", headers)
    res = conn.getresponse()
    data = res.read().decode("utf-8")
    dot_data = json.loads(data)
    dot_price = round(float(dot_data["price"]), 2)
    print(dot_price)
    
    buy_dot = False
    
    if dot_price < 8.70:
        buy_dot = True 
        
    if buy_dot:
        client = Client(TWILIO_SID, TWILIO_API)
        message = client.messages.create(
            body="Buy some DOT ma boi!!!",
            from_="+18885998708",
            to="+16302012552"
        )
        print(message.status)
    else:
        client = Client(TWILIO_SID, TWILIO_API)
        message = client.messages.create(
            body="HODL like vice grips!",
            from_="+18885998708",
            to="+16302012552"
        )
        print(message.status)

if __name__ == "__main__":
    crypto_pair = "DOT-USD"  
    fetch_public_product_http_client(crypto_pair)
