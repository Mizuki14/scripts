#!/usr/bin/python
# Created by Mizuki Hachisuka 15/11/2021

# https://api.github.com/
# https://www.techgeekbuzz.com/how-to-use-github-api-in-python/

#Libraries
from prettytable import PrettyTable
from github import Github
import subprocess
import requests
import argparse

#Access-token
access_token = Github("")
github_username = "Mizuki14"

#def universal object
table = PrettyTable()

def getUserData():
    #def and inilize
    
    table.field_names = ["Key", "Value"]
    
    api_url =f"https://api.github.com/users/{github_username}" 

    #send get request
    response = requests.get(api_url)

    #get the data in json or equivalent dict format
    data =  response.json()

    for key, value in data.items():
        table.add_row([key, value])

    print(table)
    
def getRepoInfo():
    #def and initilize
    table.field_names = ["Repository Name", "Created Date", "Last Modifiedclear"]

    #api url to grab public user repositories
    api_url = f"https://api.github.com/users/{github_username}/repos"
    
    print("Attenmpting to connect.... ")
    
    try:
        print("successful")
        
    except:
        print("error. ")
        
    #send get request
    response = requests.get(api_url)

    #get the json data
    data =  response.json()

    for repository in data:
        table.add_row([repository["name"], repository["created_at"], repository["updated_at"]])

    print(table)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #list functions
    FUNCTION_MAP = {'get repositories data' : getRepoInfo,
                'get user public info' : getUserData}

    parser.add_argument('command', choices=FUNCTION_MAP.keys())

    args = parser.parse_args()

    func = FUNCTION_MAP[args.command]
    func()

