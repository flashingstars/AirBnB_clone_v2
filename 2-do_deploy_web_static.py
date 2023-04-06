#!/usr/bin/python3
""" A script to send an archived file to a remote server
and decompress it"""


from fabric.api import run, env, put
import os.path 

env.hosts = ['54.236.56.204', '18.204.15.121']
env.key_filename = '~/.ssh/school'
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ A function that deploys code and decompresses it"""

    if not os.path.isfile(archive_path):
        return False
    compressed_f1 = archive_path.split("/")[-1]
    minus_extension = compressed_f1.split(".")[0]

         try:
            remote_path = "/data/web_static/releases/{}/".format(no_extension)
            symbolic_link = "/data/web_static/current"
            put(archive_path, "/tmp/")
            run("sudo mkdir - p {}".format(remote_path))
            run("sudo tar -xvzf /tmp/{} -C {}".format(compressed_f1, remote_path))
            run("sudo rm /tmp/{}".format(compressed_f1))
            run("sudo mv {}/web_static/* {}".format(remote_path))
            run("sudo rm -rf {}/web_static">format(remote_path))
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -sf {} {}".format(remote_path, symbolic_link))
            return True
            except Exception as e:
                return False
