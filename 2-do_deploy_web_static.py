#!/usr/bin/python3
'''Module 2-do_deploy_web_static
Distributes an archive to your web servers, using do_deploy() 
'''
from fabric.api import *
import os


env.hosts = ['18.232.153.3', '34.236.33.185']
def do_deploy(archive_path):
    '''Deploys archive to remote servers'''

    file_path = os.getcwd() + '/' + archive_path
    # Return false if the archive doesn't exist
    try:
        os.path.getsize(os.getcwd() + '/' + archive_path)
    except Exception:
        return False
    
    # Upload the archive to remote servers
    put(file_path, "/tmp/")
    run('mkdir -p /data/web_static/releases/')
    run('sudo tar zxvf /tmp/' + archive_path[9:] + ' -C /data/web_static/releases/')
    run('sudo rm /tmp/' + archive_path[9:])
    run('sudo ln -sf /data/web_static/releases/ /data/web_static/current')
