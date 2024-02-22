import requests
import asyncio


API = "https://www.cbr-xml-daily.ru/latest.js"

        
    
def getCurse():
    response = requests.get(API)
    data = response.json()
    return data