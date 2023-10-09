''' Class takes care of talking to google sheet '''
import requests


class DataManager:
    ''' Functionality for crud operations on Google Sheet.'''
    def __init__(self, auth_sheetly, url_endpoint):
        self.auth_sheetly = auth_sheetly
        self.url_endpoint = url_endpoint
        self.headers = {'Authorization': self.auth_sheetly}

    def get_rows_sheetly(self):
        response = requests.get(self.url_endpoint,  headers = self.headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data['prices']

    def post_rows_sheetly(self, json):
        response = requests.post(self.url_endpoint, json=json, headers=self.headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(data)

    def update_row_sheetly(self, id, json):
        url = f"{self.url_endpoint}/{str(id)}"
        response = requests.put(url, json=json, headers=self.headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(data)
        