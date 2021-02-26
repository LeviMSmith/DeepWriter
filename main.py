import requests

from keys import key

url = "https://wordsapiv1.p.rapidapi.com/words/"

headers = {
    'x-rapidapi-key': key,
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"
    }

response = requests.request("GET", url + "no", headers=headers)

print(response.text)