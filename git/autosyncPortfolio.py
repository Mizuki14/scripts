#!/usr/bin/python
# Created by Mizuki Hachisuka 15/11/2021

# https://api.github.com/
# https://www.techgeekbuzz.com/how-to-use-github-api-in-python/

#Libraries
import json
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

def getAllURL():
    #def and inilize
    
    table.field_names = ["Name of URL", "URL"]
    
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
    
    # try:
    #     print("successful")
        
    # except:
    #     print("error. ")
        
    #send get request
    response = requests.get(api_url)
    
    #get the json data
    data =  response.json()
    #print(data)
    

    for repository in data:
        table.add_row([repository["name"], repository["created_at"], repository["updated_at"]])

    print(table)
if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    
    #add options (function) to select from
    parser.add_argument('operation', help = 'One of "getAllURL", "getRepoInfo"')
    
    args = parser.parse_args()
    
    operation = args.operation
    
    operations = {
        'getAllURL' : getAllURL, 
        'getRepoInfo' : getRepoInfo
    }

    action = operations.get(operation, lambda: print('{}: no such operation'.format(operation)))
    action()