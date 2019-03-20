# pCarrotAAC
<brief description here pls :)>

## Getting Started
These instructions will get you a copy of the project up and running on your local Ubuntu machine for development and testing purposes.

### Installation
Our first step will be to install all of the pieces that we need from the Ubuntu repositories. We will install pip, the Python package manager, to manage our Python components.

We will also get the Python development files necessary to build uWSGI.
```
sudo apt update
sudo apt install python3-pip python3-dev build-essential libssl-dev libffi-dev python3-setuptools
```
Next, we'll set up a virtual environment in order to isolate our Flask application from the other Python files on the system.

Start by installing the python3-venv package, which will install the venv module:
```
sudo apt install python3-venv
```
Next, let's clone the repository. Move into the directory after the cloning process is complete:
```
git clone https://github.com/amatria/pCarrotAAC.git
cd pCarrotAAC
```
Create a virtual environment to store your Flask project's Python requirements by typing:
```
python3.6 -m venv env
```
This will install a local copy of Python and pip into a directory called env within your project directory.

Before installing applications within the virtual environment, you need to activate it. Do so by typing:
```
source env/bin/activate
```
Your prompt will change to indicate that you are now operating within the virtual environment.

Now, let's install the requirements in our local instance of pip:
```
pip install -r requirements.txt
```
Next, let's add a rule to the UFW firewall to check that our application is running:
```
sudo ufw allow 5000
```
Now, you can test the application by typing:
```
python wsgi.py
```
!! Note that you must configurate the application for it to run smoothly. !!
