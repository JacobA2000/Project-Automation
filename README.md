# Project-Automation
**CONFIGURATION INSTRUCTONS:**  
On the first run the program will ask you for 3 things:  
1. The directory you want to clone projects to
1. Your GitHub username
1. A GitHub personal access token (You can get one here: https://github.com/settings/tokens)

This is done as a config.json file with this structure is created, you can come back and change the details later by editing the file.    
```json
{
    "projectsDir": "path to projects folder",
    "gitUsername": "username",
    "gitToken": "token"
}
```

**IF YOU ARE RUNNING LINUX YOU MAY NEED TO RUN:**  
```
chmod u+r+x gitclone.sh
```
This will ensure the gitclone.sh file has the required permissions.


**RUN THE TOOL:**  
Depending on your system you will need to run one of these commands when in the same directory as the AutomateProject.py file.
```
python3 AutomateProject.py
python AutomateProject.py
py AutomateProject.py
```
*(This will probably be changed to a terminal command later on)*
