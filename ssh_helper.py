#!/usr/bin/env python -tt
import json
import os
import curses
import subprocess

__author__ = "Logan Schmidt (d4rkd0s)"
__copyright__ = "Copyright 2018 d4rkd0s"
__credits__ = ["Logan Schmidt"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Logan Schmidt"
__email__ = "d4rkd0s@gmail.com"
__status__ = "Production"

# Your username
username = ""

# Loads the database from connections.json file in ~/.ssh/
def loadDB():
    database_file = open("/home/" + username + "/.ssh/connections.json", "r")
    return json.loads(database_file.read())

def createNewDB():
    database_file = open("/home/" + username + "/.ssh/connections.json", "w")
    data = {}
    config = open("/home/" + username + "/.ssh/config", "r")
    config_lines = config.readlines()
    num_of_lines = 0
    for line in config_lines:
        if line.find("Host ") != -1:
            text = line.rstrip('\n')
            num_of_lines += 1
            data[num_of_lines] = text[5:]
    database_file.write(json.dumps(data))
    return loadDB()

def prepareDB():
    exists = os.path.isfile("/home/" + username + "/.ssh/connections.json")
    if exists:
        return loadDB()
    else:
        createNewDB()

def printDB(database):
    for key, value in database.items():
        print(key + " - " + value)

def main():
    database = prepareDB()
    printDB(database)
    choice = input("Enter server #: ")
    cmd = ['ssh', database[choice]]
    subprocess.call(cmd)
    exit()

main()
