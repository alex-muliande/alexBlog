import requests,json

def get_quotes():
    response = requests.get('http://quotes.stormconsultancy.co.uk/random.json')
    quotes = response.json()

    return quotes