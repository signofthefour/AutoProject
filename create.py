import sys
import os
from github import Github

path = "/home/nguyendat/MyProjects/"
username = "yourGithubAccount" #Insert your github username here
password = "yourGithubPassword" #Insert your github password here


def create():
    folderName = str(sys.argv[1])
    for root, directories, f in os.walk(path):
        for dir in directories:
            if dir == folderName:
                print("There was a repo with this name before")
                return
    os.makedirs(path + str(folderName))
    g = Github(username, password)
    user = g.get_user()
    repo = user.create_repo(folderName)
    # for repo in user.get_repos():
    #     print(repo.name)
    print("Succesfully created repository {}".format(folderName))


if __name__ == "__main__":
    create()