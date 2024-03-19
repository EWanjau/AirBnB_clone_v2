#!/usr/bin/python3
"""The module zips the files and folders ready for deployment
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Function to generate a tgz from web_static"""
    try:
        local("mkdir -p versions")
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        tgz_file = "versions/web_static_{}.tgz".format(date)
        local("tar -czvf {} web_static".format(tgz_file))
        return tgz_file
    except:
        return None
