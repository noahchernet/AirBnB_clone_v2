#!/usr/bin/python3
'''Module 3-deploy_web_static
Streamlines website deployment. Creates archive of the website,
puts the archive on the web servers and makes the site available to
view'''

from fabric.api import *
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['18.232.153.3', '34.236.33.185']


def deploy():
    '''Deploys latest version of web_static to the servers'''
    archive_name = do_pack()
    if archive_name:
        output = do_deploy(archive_name)
        return output
    return False
