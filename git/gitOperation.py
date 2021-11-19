#!/usr/bin/python
# Created by Mizuki Hachisuka 18/11/2021
import json
from prettytable import PrettyTable
from github import Github
import subprocess
import requests
import argparse
import 


def gitPull():
    pull_URL = 