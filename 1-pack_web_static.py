#!/usr/bin/python3
"""The module zips the files and folders ready for deployment
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        now = datetime.now()
        date_format = now.strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date_format)
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None
