# Project-Automation
**CONFIGURATION INSTRUCTONS**  
Create a config.json file in the same directory as the AutomateProject.py file, following the template below, but replacing path, username and token with your details.

```json
{
    "projectsDir": "path to projects folder",
    "gitUsername": "username",
    "gitToken": "token"
}
```

*(Currently working on a system where this will be created by the user via the python script using inputs on the first run.)*

**IF YOU ARE RUNNING LINUX YOU MAY NEED TO MAKE SURE THE gitclone.sh FILE HAS THE CORRECT PERMS TO RUN**  
To ensure this is the case run chmod u+r+x gitclone.sh


**RUN THE TOOL**  
Depending on your system you will need to run one of these commands when in the same directory as the AutomateProject.py file.
```
python3 AutomateProject.py
python AutomateProject.py
py AutomateProject.py
```
*(This will probably be changed to a terminal command later on)*
