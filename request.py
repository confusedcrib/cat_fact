import requests, json

def function():
    url = requests.get('https://cat-fact.herokuapp.com/facts')

    cat_dict = url.json()

    print(cat_dict['all'][1]['text'])

function()