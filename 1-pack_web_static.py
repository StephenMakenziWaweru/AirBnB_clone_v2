"""Fabfile to create a .tgz archive"""
import fabric.api
from datetime import datetime
import os


def do_pack():
    """creates a .tgz archive"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"versions/web_static_{date}.tgz"
    if not os.path.exists("/versions/"):
        local("mkdir versions/")
    local("tar -cvzf {} web_static".format(file_name))
    if os.path.exists(filename):
        return filename
    else:
        return None
