''' Using Pixela to track a habit, docs at https://pixe.la '''
from datetime import datetime
import os
from dotenv import load_dotenv
import requests

load_dotenv()

PIXELA_BASE_URL = "https://pixe.la/v1/users"
PIXELA_USERNAME = "balcoder"
PIXELA_TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_PARAMS = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
    }

PIXELA_GRAPH_URL = f"{PIXELA_BASE_URL}/{PIXELA_USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "Swiming Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

def create_pixela_account():
    ''' create a user account '''
    response = requests.post(PIXELA_BASE_URL, json=PIXELA_PARAMS, timeout=10)
    print(response.text)

def create_new_graph():
    ''' create a new graph '''
    response = requests.post(PIXELA_GRAPH_URL,  json=graph_config, headers=headers, timeout=10)
    print(response.text)

def post_pixel(quantity: str, today = datetime.today().strftime('%Y%m%d')):
    ''' It records the quantity of the specified date as a "Pixel" to graph '''
    # today = datetime.today().strftime('%Y%m%d')
    # quantity = input("Hom many Km did you swim today?")
    graph_update = {
        "date": today,
        "quantity": quantity,
        "optionalData": "{\"conditions\": \"Rough\"}"
    }

    response = requests.post(
        f"{PIXELA_GRAPH_URL}/{GRAPH_ID}",
        json=graph_update,
        headers=headers,
        timeout=10
        )
    print(response.text)

# post_pixel("1.4","20230909")

def update_pixel(date, quantity):
    ''' Update the quantity already registered as a "Pixel". If target "Pixel"
    not exist, create a new "Pixel" and set quantity. '''
    pixel_update = {
        "quantity": quantity
    }
    response = requests.put(
        f"{PIXELA_GRAPH_URL}/{GRAPH_ID}/{date}",
        json=pixel_update,
        headers=headers,
        timeout=10
        )
    print(response.text)

# update_pixel("20230912", "1.1")

def delete_pixel(date: str):
    ''' Delete the registered "Pixel". '''    
    response = requests.delete(
        f"{PIXELA_GRAPH_URL}/{GRAPH_ID}/{date}",        
        headers=headers,
        timeout=10
        )
    print(response.text)

# delete_pixel("20230910")
