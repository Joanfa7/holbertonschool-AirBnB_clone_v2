#!/usr/bin/python3
#create a tgz file
import os.path
from fabric.api import local
from datetime import datetime


def do_pack():
    """ do_pack funtion"""
    dt = datetime.now().strftime("%Y%m%d%H%M%S")
    fileName = "versions/web_static_{}.tgz".format(dt)
    if os.path.isdir("versions") is False:
        local("mkdir version")
    try:
        local("tar -cvzf {} web_static".format(tgzname))
        return tgzname
    except:
        return None
