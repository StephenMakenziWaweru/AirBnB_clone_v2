#!/usr/bin/python3
"""Deploys compressed files to webservers"""
from fabric.api import *
import os

# define hosts and user
env.hosts = [
        "34.139.26.238",
        "18.207.4.175",
        ]
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Deploys.gz archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    filename = os.path.basename(archive_path)
    filename_ext = filename.split(".")[0]
    new_dir = "/data/web_static/releases/" + filename_ext
    put(archive_path, '/tmp/')
    run(f"mkdir -p {new_dir}")
    run(f"tar -xzf /tmp/{filename} -C {new_dir}")
    
    run(f"rm /tmp/{filename}")
    run(f"mv {new_dir}/web_static/* {new_dir}")
    run(f"rm -rf {new_dir}/web_static")
    run("rm -rf /data/web_static/current")
    run(f"ln -s {new_dir} /data/web_static/current")

    return True
