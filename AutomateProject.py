import requests
import json
import subprocess
import os
import sys

#Terminal Colours
class Color():
    RED = '\033[91m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'

#Path this file is stored at.
myPath = os.path.dirname(os.path.abspath(__file__))
configPath = f"{myPath}\\config.json"

#if not windows presume linux
if os.name != "nt":
    configPath = f"{myPath}/config.json"

projectsDir = ""
gitUsername = ""
gitToken = ""

#Get config data from config.json file
with open(configPath, "r") as f:
    configData = json.load(f)
    projectsDir = configData["projectsDir"]
    gitUsername = configData["gitUsername"]
    gitToken = configData["gitToken"]    

#Get the project name the user wants.
projectName = input("Project Name: ")

#Send the request to the GitHub API
url = "https://api.github.com/user/repos"
payload = {
    "name": projectName, 
    "private": True, 
    "auto_init": True
    }

r = requests.post(url, auth=(gitUsername, gitToken), data=json.dumps(payload))

#Convert the resposnse string to json
rJson = json.loads(r.text)

#Check if there was a response message
if "message" in rJson:
    msg = rJson["message"]
    print(f"{Color.RED}Message: {msg}{Color.ENDC}")

    #Check for any errors
    if "errors" in rJson:
        errors = rJson["errors"]
        errorMsg = ""

        for error in errors:
            errorMsg += f"{error['message']}, "

        errorMsg = errorMsg[:-2]

        print(f"{Color.RED}Errors: {errorMsg}{Color.ENDC}")

else:
    #Requires chmod u+r+x gitclone.sh to be run first on linux
    #Call our gitclone shell script to clone the project to the users project folder
    print(f"{Color.GREEN}Cloning repo from GitHub to{Color.ENDC} {Color.CYAN}{projectsDir}{projectName}{Color.ENDC}")
    
    cloneLocation = f"{projectsDir}{rJson['name']}"

    if os.name == "nt":
        subprocess.call([f"{myPath}\gitclone.sh", projectsDir, rJson["ssh_url"]], shell=True)
        subprocess.Popen(f"explorer /sepearte, {cloneLocation}")
    else:
        subprocess.call([f"{myPath}/gitclone.sh", projectsDir, rJson["ssh_url"]])