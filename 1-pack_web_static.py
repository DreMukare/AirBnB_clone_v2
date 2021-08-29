#!/usr/bin/python3
'''
fabric script that generates a .tgz archive from
the contents of web_static/
'''
from fabric.api import local
from datetime import datetime
from os import path


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
