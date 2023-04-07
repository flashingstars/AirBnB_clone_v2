#!/usr/bin/python3
"""Deploying an archived file to the server
"""
from fabric.api import local
from datetime import datetime
from fabric.api import env, put, run
import os.path

# Remote hosts ip addresses
env.hosts = ["54.236.56.204", "18.204.15.121"]


def do_pack():
    """" Compressing a file and returning its path """

    # Creating timestamp and filename
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(time_now)

    try:
        # Creating versions directory
        local("mkdir -p versions")

        # Creating an archived file
        local("tar -cvzf {} web_static/".format(file_path))

        # Returning path to the archived file
        return "{}".format(file_path)

        # Return none on error
    except Exception as e:
        return None


def do_deploy(archive_path):
    """ A function that deploys an archive to the web servers """

    if not os.path.isfile(archive_path):
        return False

    # Removing extension from the file name
    file_path = archive_path.split("/")[-1]
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


def deploy():
    """ Deploying """
    file_path = do_pack()
    if file_path is None:
        return False
    return do_deploy(file_path)
