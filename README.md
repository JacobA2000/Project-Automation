# Project-Automation
## Contents:
1. [Configuration](#configuration)
1. [Linux Specific Requirements](#linux-requirements)
1. [Running The Tool](#running-the-tool)
    * [As a Terminal Command](#as-a-terminal-command)
        * [Windows](#windows)
        * [Linux](#linux)
    * [Directly via Python](#directly-via-python)



## Configuration:
**CONFIGURATION INSTRUCTONS:**  
**You will need to setup a ssh key for your device to access GitHub**, details on this can be found here: [GitHub SSH Setup](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/connecting-to-github-with-ssh)  

**MAKE SURE TO RUN setup.py FIRST ON FIRST RUN**  
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

## Linux Requirements:
**IF YOU ARE RUNNING LINUX YOU MAY NEED TO RUN:**  
```
chmod u+r+x gitclone.sh
chmod u+r+x createproj.sh
```
This will ensure the gitclone.sh and the createproj.sh file have the required permissions.


## Running the Tool:
**IMPORTANT - ON FIRST RUN MAKE SURE TO RUN THE SETUP SCRIPT FIRST**  
There are 2 ways to run this tool:
1. As a terminal commmand (prefered use but more complicated setup)
1. Directly via Python

### As a Terminal Command:
When you ran the setup.py file a .sh or .bat file was created depending on your OS. This is a file that the operating system's terminal can natively run and all it does is tells the terminal to run our AutomateProject Python script, however to achieve this there is some manual setup.

#### Windows:
On windows we need to add our Project-Automation folder to our PATH environment variable. To do this we need to do the following:
1. Open the search bar and search for "edit environment variables for you account" and open it.
1. Click on the path variable in the user variables and hit edit.
1. Copy the path to the folder you saved the script in.
1. Hit new and paste the path we copied.
1. Press OK on both windows.

Now we should be able to open up a terminal(powershell, cmd, windows terminal, etc) and type createproj and it will execute the python script.

#### Linux:
On Linux we need to add our Project-Automation folder to our PATH environment variable. To do this we need to do the following:
1. cd into the projects directory
1. Make sure our shell script has the right permissions (this was shown above and doesn't need to be repeated if you have already done so):
    ```
    chmod u+r+x createproj.sh
    ```
1. cd to your home directory
    ```
    cd $HOME
    ```
1. Open up your terminals rc file (this file name varies depending on your terminal but in most distros, the default will be .bashrc, I have included some popular terminals rc files below) with your favourite text editor(I would recommend using vim)
    ```
    bash: ~/.bashrc

    zsh: ~/.zshrc
    ```
1. Add the following line, **MAKE SURE TO CHANGE /path/to/project/folder TO THE PATH YOU SAVED THE PROJECT AT**  
    ```
    export PATH=/path/to/project/folder:$PATH
    ```
1. Reboot your machine

Now we should be able to open up the terminal and run our shell script by typing createproj.sh 

### Directly via Python:  
Depending on your system you will need to run one of these commands when in the same directory as the AutomateProject.py file.
```
python3 AutomateProject.py
python AutomateProject.py
py AutomateProject.py
```