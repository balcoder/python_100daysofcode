'''Load destinations and max price from a google doc and check available
flights. If cheap flight found, then send sms to phone'''

import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

load_dotenv()
URL_ENDPOINT_SHEETLY = "https://api.sheety.co/6c1ed1c6402dc0affae911b515bfc3ca/flightDeals/prices"
LOCATIONS_ENDPOINT = "https://api.tequila.kiwi.com"
BASIC_AUTH_SHEETLY = os.getenv('BASIC_AUTH_SHEETLY')
LOCATIONS_API_KEY = os.getenv('LOCATIONS_API')
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')

DATA_MANAGER = DataManager(BASIC_AUTH_SHEETLY, URL_ENDPOINT_SHEETLY)
FLIGHT_SEARCH = FlightSearch(LOCATIONS_API_KEY, LOCATIONS_ENDPOINT)
NOTIFICATION_MANAGER = NotificationManager(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def load_iata_codes():
    ''' load the flight deals sheet from google docs and return sheet data '''
    sheet_data = DATA_MANAGER.get_rows_sheetly()
    # check if iataCodes are empty and get code from flight search
    for entry in sheet_data:
        if entry['iataCode'] == '':
            airport_codes = FLIGHT_SEARCH.get_iata_code(entry['city'])
            iata_code = airport_codes['locations'][0]['city']['code']
            # update the sheet itself
            DATA_MANAGER.update_row_sheetly(id=entry['id'], json={'price': {'iataCode': iata_code}})
            # update any empty code before returning, saves making another request
            entry['iataCode'] = iata_code
    return sheet_data

def get_lowest_prices(sheet_data) -> list:
    ''' search flight search api for each destination on google sheet and return
        a list of flights that are <= to google sheet max '''
    flight_deals = []
    for iata in sheet_data:
        lowest_price = FLIGHT_SEARCH.get_prices(iata_departure_code, iata['iataCode'], iata['lowestPrice'])
        if len(lowest_price) > 0:
            if lowest_price['price'] <= iata['lowestPrice']:
                flight_deals.append(lowest_price)
    return flight_deals

def send_notification(flights:list):
    ''' get all the flights that match or cut off price and send sms '''
    for flight in flights:
        message = (
            f"Low price alert! Only {flight['price']} to fly from\n"
            f"{flight['cityFrom']}-{flight['flyFrom']} to {flight['cityTo']}-{flight['flyTo']}\n"
            f"on {flight['local_departure']} with airline {flight['airlines'][0]}"
        )
        NOTIFICATION_MANAGER.send_sms(message=message)

origin = input("What city would you like to depart from?")
locations = FLIGHT_SEARCH.get_iata_code(origin)
iata_departure_code = locations['locations'][0]['code']

# get a list of iata codes of destinations from my google doc
my_destinations = load_iata_codes()

# check the codes for prices lower than my max
matching_flights = get_lowest_prices(my_destinations)

# send an sms with low fares and flight details
send_notification(matching_flights)
