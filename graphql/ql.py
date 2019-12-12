import requests
from pathlib import Path
import json


def get(query):

    url = "https://api.github.com/graphql"
    jsone = query
    # { 'query' : '''{
    # repository(owner:"octocat", name:"Hello-World") {
    #     issues(last:20, states:CLOSED) {
    #     edges {
    #         node {
    #         title
    #         url
    #         labels(first:5) {
    #             edges {
    #             node {
    #                 name
    #             }
    #             }
    #         }
    #         }
    #     }
    #     }
    # }
    # }'''
    # }

    config = Path("./token.txt")

    if config.is_file():
        accessToken = open("token.txt", "r")
        token = accessToken.read()
    else:
        token = input("input token:")

    headers = {"Authorization": "token {}".format(token)}

    r = requests.post(url=url, json=jsone, headers=headers)
    r = json.loads(r.text)
    print(json.dumps(r, sort_keys=True, indent=4))

