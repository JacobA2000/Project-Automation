import requests
import json
import subprocess

projectsDir = ""
gitUsername = ""
gitToken = ""

#Get config data form config.json file
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
    #Call our gitclone shell script to clone the project to the users project folder
    print(f"\033[92mCloning repo from GitHub to\033[0m \033[96m{projectsDir}{projectName}\033[0m")
    subprocess.call(["./gitclone.sh", projectsDir, rJson["clone_url"]])
