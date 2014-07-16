# -*- coding: utf-8 -*-
# Django settings for OpenShift project.
import imp, os

# from project.settings import *

PROJECT_DIR = os.path.dirname(os.path.realpath(__file__))

DEBUG = bool(os.environ.get('DEBUG', False))
if DEBUG:
        print("WARNING: The DEBUG environment is set to True.")

TEMPLATE_DEBUG = DEBUG

# os.environ['OPENSHIFT_MYSQL_DB_*'] variables can be used with databases created
# with rhc cartridge add (see /README in this git repo)
DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'self.
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'python',  # Or path to database file if using sqlite3.
        'USER': os.environ['OPENSHIFT_MYSQL_DB_USERNAME'],
        'PASSWORD': os.environ['OPENSHIFT_MYSQL_DB_PASSWORD'],
        'HOST': os.environ['OPENSHIFT_MYSQL_DB_HOST'],
        'PORT': os.environ['OPENSHIFT_MYSQL_DB_PORT'],
    }
}

MEDIA_ROOT = os.environ.get('OPENSHIFT_DATA_DIR', '')
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_DIR, '..', 'static')

# Make a dictionary of default keys
default_keys = { 'SECRET_KEY': 'vm4rl5*ymb@2&d_(gc$gb-^twq9w(u69hi--%$5xrh!xk(t%hw' }

imp.find_module('openshiftlibs')
import openshiftlibs
use_keys = openshiftlibs.openshift_secure(default_keys)

# Make this unique, and don't share it with anybody.
SECRET_KEY = use_keys['SECRET_KEY']

ALLOWED_HOSTS = [os.environ.get('HOSTNAME'),]
