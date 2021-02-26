#Hi

#Word API stuff

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

#Paper generation

def generate_paper(reference_text):
    parsed_ref = parse_reference_text(reference_text)
    generate_thesis(parsed_ref)
    pass

def generate_thesis(parsed_ref):
    pass

def generate_intro():
    pass

def generate_body():
    pass

def generate_conclusion():
    pass

#Misc

def parse_reference_text(ref_txt): #Just get stuff that makes good quotes (eventually)
    f = open(ref_txt, 'r')
    return(f)

#Begin
import sys

if len(sys.argv) == 1:
    generate_paper(str(sys.argv[1]))
else:
    pass
