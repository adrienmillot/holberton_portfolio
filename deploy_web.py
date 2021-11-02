#!usr/bin/python3

from fabric.api import local, put, run, env
import os
from datetime import datetime


env.hosts = ['35.180.50.252']


def __install_nginx():
    """instal nginx"""

    try:
        run("sudo apt update")
        run("sudo apt install nginx")
        run("sudo service nginx start")
        print("Nginx installed")
        return True
    except:
        return False


def __configure_nginx():
    """configure Nginx"""
    try:
        # create symbolic link
        run("sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default")
        
        return True
    except:

        return False
