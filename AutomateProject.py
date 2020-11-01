import requests
import json
import subprocess
import os

projectsDir = ""
gitUsername = ""
gitToken = ""

if os.path.exists("config.json") == False:
    print("First Time Setup")
    projectsPath = input("Projects Path (the path you wish your projects to be cloned to) : ")
    uname = input("GitHub username : ")
    token = input("GitHub Token (your GitHub personal access token, you can get one here https://github.com/settings/tokens) : ")

    userConfig = {"projectsDir": projectsPath, "gitUsername": uname, "gitToken": token}

    with open("config.json", "w") as f:
        json.dump(userConfig, f)

#Get config data from config.json file
with open("config.json", "r") as f:
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
    print(f"\033[91mMessage: {msg}\033[0m")

    #Check for any errors
    if "errors" in rJson:
        errors = rJson["errors"]
        errorMsg = ""

        for error in errors:
            errorMsg += f"{error['message']}, "

        errorMsg = errorMsg[:-2]

        print(f"\033[91mErrors: {errorMsg}\033[0m")

else:
    #Requires chmod u+r+x gitclone.sh to be run first on linux
    #Call our gitclone shell script to clone the project to the users project folder
    print(f"\033[92mCloning repo from GitHub to\033[0m \033[96m{projectsDir}{projectName}\033[0m")
    
    if os.name == "nt":
        subprocess.call(["gitclone.sh", projectsDir, rJson["clone_url"]], shell=True)
    else:
        subprocess.call(["./gitclone.sh", projectsDir, rJson["clone_url"]])
