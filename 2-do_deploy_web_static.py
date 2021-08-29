#!/usr/bin/python3
'''
fabric script that generates a .tgz archive from
the contents of web_static
distributes archive to web servers
'''
from fabric.api import *
from datetime import datetime
from os import path



env.user = 'ubuntu'
env.hosts = ['34.75.183.8', '34.139.231.119']

def do_deploy(archive_path):
    ''' distributes archive to web servers '''
    file = archive_path.split('/')[-1]
    name = archive_path.split('.')[0]
    if path.isfile(archive_path):
        if put(archive_path, '/tmp/{}'.format(file)).failed is True:
            return False
        if run('tar -xvzf /tmp/{} -C /data/web_static/releases/{}'.format(
            file, name)).failed is True:
                return False
        if sudo('rm /tmp/{}'.format(archive_path)).failed is True:
            return False
        if sudo('rm /data/web_static/current').failed is True:
            return False
        if run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(name)).failed is True:
            return False
        return True        
    return False
