from github import Github
from pathlib import Path

config = Path("./token.txt")

if config.is_file():
    accessToken = open("token.txt", "r")
    token = accessToken.read()
else:
    token = input("input token:")


g = Github(token)

org = g.get_organization_membership("ucsb-cs16-mirza")
print(org)


def getMethods(nam):
    object_methods = [
        method_name for method_name in dir(nam) if callable(getattr(nam, method_name))
    ]

