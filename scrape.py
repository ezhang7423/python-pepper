import requests




url = 'https://api.github.com/graphql'
json = { 'query' : '{ viewer { repositories(first: 30) { totalCount pageInfo { hasNextPage endCursor } edges { node { name } } } } }' }

config = Path('./token.txt')

if config.is_file():
    accessToken = open('token.txt', 'r')
    token = accessToken.read()
else:
    token = input('input token:')


headers = {'Authorization': 'token {}'.format(token)}

r = requests.post(url=url, json=json, headers=headers)
print (r.text)
