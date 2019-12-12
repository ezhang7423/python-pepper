import requests
from pathlib import Path



url = 'https://api.github.com/graphql'
json = { 'query' : '''{
  repository(owner:"octocat", name:"Hello-World") {
    issues(last:20, states:CLOSED) {
      edges {
        node {
          title
          url
          labels(first:5) {
            edges {
              node {
                name
              }
            }
          }
        }
      }
    }
  }
}'''
}

config = Path('./token.txt')

if config.is_file():
    accessToken = open('token.txt', 'r')
    token = accessToken.read()
else:
    token = input('input token:')


headers = {'Authorization': 'token {}'.format(token)}

r = requests.post(url=url, json=json, headers=headers)
print(r.text)