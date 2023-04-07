#!/usr/bin/python3
"""Deploying the webstatic to the server
"""
from fabric.api import env, put, run
import os

# Remote hosts ip addresses
env.hosts = ["54.236.56.204", "18.204.15.121"]


def do_deploy(archive_path):
    """ A function that deploys an archive to the web servers """

    if not os.path.isfile(archive_path):
        return False

    # Removing extension from the file name
    file_path1 = archive_path.split("/")[-1]
    dir_name = file_path.split(".")[0]

    dir_path = "/data/web_static/releases/{}".format(dir_name)
    try:
        # Placing archive to temporary folder
        put(archive_path, "/tmp/")
        # Directory to deploy code
        run("sudo mkdir -p {}".format(dir_path))
        # Removing compression
        run("sudo tar -xvzf /tmp/{} -C {}".format(file_path1, dir_path))
        run("sudo rm /tmp/{}".format(file_path1))
        # Moving files to a new folder
        run("sudo mv {}/web_static/* {}".format(dir_path, dir_path))
        run("sudo rm -rf {}/web_static".format(dir_path))
        # Removing the old symbolic link and creating a new one
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -sf {} /data/web_static/current".format(dir_path))
    except Exception as e:
        # Return false if there is an error
        return False
    return True
