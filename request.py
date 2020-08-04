import requests, json, random

def function():
    url = requests.get('https://cat-fact.herokuapp.com/facts')

    cat_dict = url.json()

    cat = random.randint(1, 100)

    print(cat_dict['all'][cat]['text'])

function()