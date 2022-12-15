import requests
from model.api_fields import ApiField

class RequestManager:
    """
    Author  : Amine
    Version : 1
    Date    : 15/12/2022
    Description : this class handles the request to API and returning simple exploitable data as tha state for charge and data

    """
    def __init__(self, url):
        # this class handles interacting with the API and returning usefel data 
        self.records:list = []
        response = requests.get(url)
        if(response.status_code == 200):
            for record in response.json()['records']:
                self.records.append(ApiField(**(record['fields'])))
        else :
            return response.status_code