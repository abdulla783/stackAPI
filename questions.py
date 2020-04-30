import requests


q = 'python try except error'
title = 'python try except error'
tagged = 'python'

def make_request(q, title, tagged):
    url = 'https://api.stackexchange.com/' + f'2.2/search/advanced?order=desc&sort=activity&q={q}&accepted=False&answers=1&tagged={tagged}&title={title}&site=stackoverflow'
    resp = requests.get(url)
    return resp.json()

query = make_request(q, title, tagged)

def get_urls(json_dict):
    url_list = []
    for i in json_dict["items"]:
        if i["is_answered"]:
            url_list.append(i["link"])
    print(url_list)

get_urls(query)