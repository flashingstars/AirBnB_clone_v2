#!/usr/bin/python3
"""Deploying the webstatic to the server
"""
from fabric.api import env, put, run
import os

env.hosts = ["54.236.56.204", "18.204.15.121"]


def do_deploy(archive_path):
    """ A function that deploys and decompresses code """
    
if not os.path.isfile(archive_path):
        return False

    file_path1 = archive_path.split("/")[-1]
    dir_name = file_path.split(".")[0]

    dir_path = "/data/web_static/releases/{}".format(dir_name)
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(dir_path))
        run("sudo tar -xvzf /tmp/{} -C {}".format(file_path1, dir_path))
        run("sudo rm /tmp/{}".format(file_path1))
        run("sudo mv {}/web_static/* {}".format(dir_path, dir_path))
        run("sudo rm -rf {}/web_static".format(dir_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} /data/web_static/current".format(dir_path))
    except Exception as e:
        return False
    return True
