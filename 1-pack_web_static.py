#!/usr/bin/python3
"""A python script to create an archived fabfile"""
from fabric.api import local
from datetime import datetime

def do_pack():
    """ A method to compress a file and return its path """
    
    """saving the timestamp and creating a filename"""
    time_now = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(time_now)
   
    try:
        """creating a directory called versions"""
        local("mkdir -p versions")
         
        """creating an archive file"""
        local("tar -cvzf {} web_static/".format(file_path))
        
        """Path to the archive file created"""
        return "{}".format(file_path)

        """Incase of an error"""
    except Exception as e:
        return None
