# -*- coding: utf-8 -*-
__author__ = 'alex'
import os
import sys

OS_RUNING = sys.platform
SOFTWARE_NAME = "Pyclue"
VERSION = "0.1"
AUTHOR = "Alex Dzul"
AUTHOR_EMAIL = "alexexc2@gmail.com"
LICENCE = "GPL v2"
SECRET_KEY = 'mysecretpassword'


PROJECT_DIR = "pyclue"
RESOURCES_DIR = 'resources'

if OS_RUNING == "darwin":
    APP_ICON = os.path.join(RESOURCES_DIR, 'img/key.ico')
else:
    APP_ICON = os.path.join("%s/%s" % (PROJECT_DIR, RESOURCES_DIR), ' img/key.ico')
    
DB_NAME = 'pyclue.db'


WELCOME_MESSAGE = "Before starting using this application, " \
                  "it is necessary that you enter some basic " \
                  "information"

ABOUT_MESSAGE = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">PyClue.</span>" \
                "</p><p>Is an Open Source password manager which simplifies the task of </p><p>grouping secret " \
                "information in one place. </p><p>This software is cross-platform because it is written in Python." \
                "</p><p><span style=\" font-size:12pt; font-weight:600;\">Author.</span></p><p>Alex Dzul. Twitter: " \
                "<a href=\"http://www.twitter.com/alexjs88\"><span style=\" text-decoration: underline; color:#0000ff;\">" \
                "@alexjs88</span></a></p><p><span style=\" font-size:12pt; font-weight:600;\">Licence.</span></p><p>" \
                "This software is under the GPL v2 terms.</p><p>Copyright (C) 2014, version."+ VERSION +"</p><p><span style=\" font-size:12pt; " \
                "font-weight:600;\">Github.</span></p><p>View the code on <a href=\"https://github.com/alexdzul/Pyclue\">" \
                "<span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/alexdzul/Pyclue</span></a>" \
                "<br/></p></body></html>"


def get_data_path():
    from os.path import expanduser
    try:
        if OS_RUNING == "darwin": # if it's running on MAC
            path = expanduser("~")
            database_file = "%s/Library/%s/data/%s"%(path, SOFTWARE_NAME, DB_NAME)
        else:
            database_file = "data/%s" % DB_NAME
    except:
        database_file = None
    return database_file


def get_backup_path():
    from os.path import expanduser
    try:
        if OS_RUNING == "darwin": # if it's running on MAC
            path = expanduser("~")
            database_file = "%s/Library/%s/backups"%(path, SOFTWARE_NAME)
        else:
            database_file = "backups"
    except:
        database_file = None
    return database_file


# ====================================================================================
# Functions to create the primary paths.
# ========================================================================================

def create_default_backups_path():
    if OS_RUNING == "darwin":
        from os.path import expanduser
        path = expanduser("~")
        path = "%s/Library/%s/backups/" % (path, SOFTWARE_NAME)
    else:
        path = "backups"
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            return True
    except:
        return False


def create_data_path():
    """
    Función para crear el path donde irá almacenada la base de datos.
    :return: True or False
    """
    from os.path import expanduser
    if OS_RUNING == "darwin":
        path = expanduser("~")
        path = "%s/Library/%s/data/"%(path, SOFTWARE_NAME)
        print(path)
    else:
        path = "data"
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            return True
    except:
        return False