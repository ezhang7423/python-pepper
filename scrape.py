from github import Github
from pathlib import Path

config = Path('./token.txt')

if config.is_file():
    accessToken = open('token.txt', 'r')
    token = accessToken.read()
else:
    token = input('input token:')

    
g = Github(token)

print(g)