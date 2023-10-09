from datetime import datetime, timedelta
import requests


class FlightSearch:
    '''This class is responsible for talking to the Flight Search API.'''
    def __init__(self, api_key, url_endpoint):
        self.api_key = api_key
        self.url_endpoint = url_endpoint
        self.headers = {"accept": "application/json", "apikey": api_key}
        self.departure_airport_code = 'LON'
        # self.departure_city = departure_city
        self.max_price = 200.00

    def get_iata_code(self, name):
        ''' given a city name return airport iata codes '''
        url = self.url_endpoint + "/locations/query"
        params = {
            'term': name,
            'locale': 'en-US',
            'location_types': 'airport',
            'limit': '10',
            'active_only': 'true'
        }

        response = requests.get(url, params=params, headers=self.headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # print(data)
            return data

        print("Request failed with status of: ", response.status_code)

    def get_prices(self, departure_airport_code, destination, max_price: int):
        ''' given destination and max price return flight details of lowest price '''
        url = self.url_endpoint + "/v2/search"
        today = datetime.now()
        tomorrow = today + timedelta(1)
        date_from = tomorrow.strftime('%d/%m/%Y')
        date_to_unformated = tomorrow + timedelta(30)
        date_to = date_to_unformated.strftime('%d/%m/%Y')
        params = {
            'fly_from': departure_airport_code,
            'fly_to': destination,
            'date_from': date_from,
            'date_to': date_to,
            'cur': 'EUR',
            'price_to': max_price,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 30,
            "flight_type": "round",
            # "one_for_city": 1, # returns the cheapest flight 
            "max_stopovers": 0,
            'limit': 20
        }

        response = requests.get(url, params=params, headers=self.headers, timeout=40)
        if response.status_code == 200:
            data = response.json()
            all_prices = []
            for deal in data['data']:
                all_prices.append(deal['price'])

            if len(all_prices) > 0:
                lowest_fare = min(all_prices)
                lowest_fare_idx = all_prices.index(lowest_fare)
                flight_details = {
                    'cityFrom': data['data'][lowest_fare_idx]['cityFrom'],
                    'flyFrom': data['data'][lowest_fare_idx]['flyFrom'],
                    'cityTo': data['data'][lowest_fare_idx]['cityTo'],
                    'flyTo': data['data'][lowest_fare_idx]['flyTo'],
                    'local_departure': data['data'][lowest_fare_idx]['local_departure'],
                    'price': data['data'][lowest_fare_idx]['price'],
                    'airlines': data['data'][lowest_fare_idx]['airlines']
                }
                return flight_details
            return {}
        print("Request failed with status of: ", response.status_code, response.text)
        