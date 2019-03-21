# pCarrotAAC

## Prerequisites
* `mysql-server` up and running.
* `nginx` installed.
* `ufw`.

## Installation
Our first step will be to install all of the pieces that we need from the Ubuntu repositories. We will pip, the Python package manager, to manage our Python components.

We will also get the Python development files necessary to build uWSGI.
```
sudo apt update && sudo apt upgrade
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
pip install wheel
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
When you have confirmed that it's functioning properly, press CTRL-C in your terminal window.

We're now done with our virtual environment, so we can deactivate it:
```
deactivate
```
You have tested that Flask is able to serve your application, but ultimately you will want something more robust for long-term usage. You can create a uWSGI configuration file with the relevant options for this.
```
nano pcarrot.ini
```
Now, paste these lines:
```
[uwsgi]
module = wsgi:app

master = true
processes = 5

socket = pcarrot.sock
chmod-socket = 660
vacuum = true

die-on-term = true
```
Next, let's create the systemd service unit file. Creating a systemd unit file will allow Ubuntu's init system to automatically start uWSGI and serve the Flask application whenever the computer boots.
```
sudo nano /etc/systemd/system/pcarrot.service
```
Inside, copy the following configuration and modify the [Service] fields:
```
[Unit]
Description=uWSGI instance to serve pcarrot
After=network.target

[Service]
User=user_running_the_service
Group=www-data
WorkingDirectory=/path/to/pCarrotAAC
Environment="PATH=/path/to/pCarrotAAC/env/bin"
ExecStart=/path/to/pCarrotAAC/env/bin/uwsgi --ini pcarrot.ini

[Install]
WantedBy=multi-user.target
```
With that, our systemd service file is complete. Save and close it now.

We can now start the uWSGI service we created and enable it so that it starts at boot:
```
sudo systemctl start pcarrot.service
sudo systemctl enable pcarrot.service
```
Our uWSGI application server should now be up and running, waiting for requests on the socket file in the project directory. Let's configure Nginx to pass web requests to that socket using the uwsgi protocol.

Begin by creating a new server block configuration file in Nginx's sites-available directory. Let's call this pcarrot to keep in line with the rest of the guide:
```
sudo nano /etc/nginx/sites-available/pcarrot
```
Open up a server block and paste:
```
server {
    listen 80;
    server_name your_domain www.your_domain;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/path/to/pcarrot/pcarrot.sock;
    }
}
```
To enable the Nginx server block configuration you've just created, link the file to the sites-enabled directory:
```
sudo ln -s /etc/nginx/sites-available/pcarrot /etc/nginx/sites-enabled
```
Restart the Nginx process to read the new configuration:
```
sudo systemctl restart nginx
```
Finally, let's adjust the firewall again. We no longer need access through port 5000, so we can remove that rule. We can then allow access to the Nginx server:
```
sudo ufw delete allow 5000
sudo ufw allow 'Nginx Full'
```
You should now be able to navigate to your server's domain name in your web browser.
