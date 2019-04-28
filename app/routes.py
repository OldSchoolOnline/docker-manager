from flask import render_template
from app import app
import docker

client = docker.from_env()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/containers')
def containers():
    containers=client.containers.list()
    return render_template('containers.html', title='Containers', containers=containers)
