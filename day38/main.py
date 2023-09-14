''' Exercise tracker with natural language processing to convert plain english
description of exercise done to amount of calories burnt. Takes that info and 
updates google sheet using sheetly api '''

import os
from datetime import datetime
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth

load_dotenv()

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_KEY = os.getenv("NUTRITIONIX_API_KEY")
BASIC_AUTH_SHEETLY = os.getenv('BASIC_AUTH_SHEETLY')
URL_ENDPOINT_NUTRIX = "https://trackapi.nutritionix.com/v2/natural/exercise"
URL_ENDPOINT_SHEETLY = "https://api.sheety.co/6c1ed1c6402dc0affae911b515bfc3ca/workoutTracking/workouts"
WEIGHT = 88.5
HEIGHT = 177.8
AGE = 50

def get_workout_stats( exercise =input("What exercises did you do?")):
    ''' given an exercise return stats in json format '''
    exercise_params ={
        "query":exercise,
        "gender":"male",
        "weight_kg":WEIGHT,
        "height_cm":HEIGHT,
        "age":AGE
        }
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(URL_ENDPOINT_NUTRIX, json=exercise_params, headers=headers, timeout=10)
    workout_data = response.json()

    now_datetime = datetime.now()
    date = now_datetime.strftime('%d/%m/%Y')
    time = now_datetime.time().strftime('%H:%M:%S')
    exercise_input = workout_data['exercises'][0]['user_input']
    duration = workout_data['exercises'][0]['duration_min']
    calories = workout_data['exercises'][0]['nf_calories']
    return {
        "workout": {
            "date":f"{date}",
            "time": f"{time}",
            "exercise": f"{exercise_input}",
            "duration": f"{duration}",
            "calories": f"{calories}"
            }}


def post_to_sheetly():
    ''' Gets workout stats from nutritionix and updates google docs using sheetly '''
    workout_stats = get_workout_stats()
    headers = {'Authorization': BASIC_AUTH_SHEETLY}
    response = requests.post(URL_ENDPOINT_SHEETLY, json=workout_stats, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()
    print(data)

post_to_sheetly()
