import os
import json

#Checks if a config file exists
if os.path.exists("config.json") == False:
    #If theres no config file create one
    print("First Time Setup")
    #Get user data to populate config file.
    projectsPath = input("Projects Path (the path you wish your projects to be cloned to) : ")

    if projectsPath.endswith("\\") == False:
        projectsPath += "\\"

    uname = input("GitHub username : ")
    token = input("GitHub Token (your GitHub personal access token, you can get one here https://github.com/settings/tokens) : ")

    userConfig = {"projectsDir": projectsPath, "gitUsername": uname, "gitToken": token}

    #Create and add data to config file.
    with open("config.json", "w") as f:
        json.dump(userConfig, f)

#Create relevant terminal script based on OS.
if os.name == "nt":
    #Checks if .bat file exists
    if os.path.exists("createproj.bat") == False:
        #Create bat file to run quickly on windows.
        with open("createproj.bat", "w") as batf:
            batf.write(f"py \"{os.getcwd()}\\AutomateProject.py\"")

else:
    if os.path.exists("createproj.sh") == False:
        #Create bat file to run quickly on windows.
        with open("createproj.sh", "w") as batf:
            batf.write(f"python3 \"{os.getcwd()}/AutomateProject.py\"")