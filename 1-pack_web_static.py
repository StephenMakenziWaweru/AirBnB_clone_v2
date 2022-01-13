#!/usr/bin/python3
"""Fabfile to create a .tgz archive"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """creates a .tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    if not os.path.exists("/versions/"):
        local("mkdir versions/")
    local("tar -cvzf {} web_static".format(filename))
    if os.path.exists(filename):
        return filename
    else:
        return None
