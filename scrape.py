from github import Github
from pathlib import Path

config = Path('./token.txt')

if config.is_file():
    accessToken = open('token.txt', 'r')
    token = accessToken.read()
    print(token)
else:
    token = input('input token:')
    print(token)

    
g = Github(token)

print(g)