#!/usr/bin/python3
'''Module 2-do_deploy_web_static
Distributes an archive to your web servers, using do_deploy()
'''
from fabric.api import *
import os

env.hosts = ['18.232.153.3', '34.236.33.185']


def do_deploy(archive_path):
    '''Calls do_deploy_run and returns either True or
    False if an exception is raised'''
    try:
        returned = do_deploy_run(archive_path)
    except Exception:
        return False
    return True if returned else False


def do_deploy_run(archive_path):
    '''Deploys archive to remote servers'''
    file_path = os.getcwd() + '/' + archive_path
    archive_name = archive_path[9:-4]

    # Return false if the archive doesn't exist
    if not os.path.isfile(file_path):
        return False

    # Upload the archive to remote servers
    put(file_path, "/tmp/")
    # If a folder with the same archive name exists, remvoe it
    run('sudo rm -rf -- /data/web_static/releases/' + archive_name)

    run('sudo mkdir -p /data/web_static/releases/' + archive_name)

    # Extract the archive's contents to
    # /data/web_static/releases/<archive_name>
    run('sudo tar zxvf /tmp/' + archive_path[9:] +
        ' -C /data/web_static/releases/' + archive_name)
    # Move the contents of the extracted archive to its parent folder
    run('sudo mv -f /data/web_static/releases/'
        + archive_name + '/web_static/* '
        + '/data/web_static/releases/' + archive_name)
    run('sudo rm -rf /data/web_static/releases/'
        + archive_name + '/web_static/')
    run('sudo rm /tmp/' + archive_path[9:])

    # '''
    # Remove the symbolic link if it exists
    run('sudo rm -f -- /data/web_static/current')
    run('sudo ln -sf /data/web_static/releases/'
        + archive_path[9:-4] + ' /data/web_static/current')
    return True
    # '''
