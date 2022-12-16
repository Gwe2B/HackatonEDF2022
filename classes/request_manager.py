import requests

from classes.model.api_fields import ApiField


class RequestManager:
    """
    Author  : Amine
    Version : 1
    Date    : 15/12/2022
    Description : This class handles the request to API and returning simple
    exploitable data as tha state for charge and corresponding date.

    """
    API_URL:str = 'https://opendata-corse.edf.fr/api/records/1.0/search/?dataset=signal-reseau-corse-recharge-vehicule-electrique&q=&rows=300&sort=-date&facet=date'

    @classmethod
    def get(cls, url):
        # this class handles interacting with the API and returning usefel data 
        cls.records:list = []
        response = requests.get(url)
        if(response.status_code == 200):
            for record in response.json()['records']:
                buf = record['fields']['date'].split('T')[1].split('+')[0].split(':')[1]
                if int(buf) == 0:
                    cls.records.append(ApiField(**(record['fields'])))
        else :
            return response.status_code