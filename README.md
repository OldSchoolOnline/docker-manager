#Docker Manager
Docker Manager is a web interface for managing Docker containers on a host. It is currently still WIP and not safe to use at all.

##Running Docker Manager
Docker Manager requires python 3 and flask to be installed.

Installation steps:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
````

Create a .flaskenv file with the following text:
```
FLASK_APP=docker-manager.py
```

Running:
```bash
flask run
```
