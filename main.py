import requests
import json

from keys import key

url = "https://wordsapiv1.p.rapidapi.com/words/"

headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }

def get_word(word):
    response = requests.request("GET", url + word, headers=headers)
    return(json.loads(response.text))

print(get_word("Hello"))