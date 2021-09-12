#!/usr/bin/python3
'''
fabric script that generates a .tgz archive from
the contents of web_static
distributes archive to web servers
'''
from fabric.api import env, put, run, local
from os import path
from datetime import datetime


env.hosts = ['34.75.183.8', '34.139.231.119']

def do_pack():
    ''' creates a .tgz archive '''
    current_date = datetime.utcnow()
    file = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
        current_date.year,
        current_date.month,
        current_date.day,
        current_date.hour,
        current_date.minute,
        current_date.second)

    if path.isdir('versions') is False:
        if local('mkdir -p versions').failed is True:
            return None
    if local('tar -cvzf {} web_static'.format(file)).failed is True:
        return None
    return file

def do_deploy(archive_path):
    '''
    distributes archive to web servers
    Args:
        archive_path(str): Path of archive to be distributed
    Returns:
        True if it succeeds, False if it fails at any point
    '''
    file = archive_path.split('/')[-1]
    name = archive_path.split('.')[0]
    if path.isfile(archive_path):
        if put(archive_path, '/tmp/{}'.format(file)).failed is True:
            return False
        if run('rm -rf /data/web_static/releases/{}/'.
               format(name)).failed is True:
            return False
        if run('mkdir -p /data/webstatic/releases/{}/'.
               format(name)).failed is True:
            return False
        if run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(
                file, name)).failed is True:
            return False
        if run('rm /tmp/{}'.format(file)).failed is True:
            return False
        if run("mv /data/web_static/releases/{}/web_static/* "
               "/data/web_static/releases/{}/".format(
                       name,
                       name)).failed is True:
            return False
        if run("rm -rf /data/web_static/releases/{}/web_static".
               format(name)).failed is True:
            return False
        if run('rm /data/web_static/current').failed is True:
            return False
        if run('ln -s /data/web_static/releases/{} /data/web_static/current'
               .format(name)).failed is True:
            return False
        return True
    return False

def deploy():
    ''' calls previous functions '''
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
