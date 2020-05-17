# Two CLI tools to calculate financial scenarios with Bitcoin

## Installation Instructions

### Windows

1. Install Python 3.6 or higher if you don't already have it
   - You can find Python 3.8 and instructions for installation at this link [Python Downloads](https://www.python.org/downloads/release/python-382/). **Make sure to pick the correct one for your operating system**
   - If you're on Windows make sure to check the **"add Python 3.8 to PATH"** checkbox when running the installer
2. Install Git
   - On Windows you can find the installer at the following link [Git Bash](https://git-scm.com/download/win)
3. Clone the repository where the program is by running the following command in git bash or cmd/Powershell if git is in your PATH
   - `git clone https://github.com/willtech3/bitcoin_hypos`







### Mac/Linux


#### Downloading the script and running it (The Easy Part)


2. Open a terminal
   - On a mac just type terminal in spotlight and one will come up
   - On windows type `cmd` in the search bar and hit enter
3. If Python installs correctly you should be able to run the command `python` in the terminal and see an interactive python interpreter come up.
   - type quit() to exit
4. Install the dependencies necessary to run the script
   - run the command below
   -  ```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib```



3. Copy the credentials file you downloaded at the end of step 9 in the previous section to the root of the repository
4. Rename the file to `client_secret.json`
5. Run the script with `python del.py`