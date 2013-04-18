# -*- coding: utf-8 -*-

import logging
import datetime as dt

DEBUG_MODE = False
LESS_DEBUG = False
JS_DEBUG = False
PRODUCTION = False

SITE = ""#your site here
SITE_DOMAIN = ""#your site here
PORT = "5000"
SECRET_KEY = "secret_keyplzchangeit"

MONGODB_DB = "zion"
MONGODB_DB_UNITTEST = "zion_unittest"
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017
MONGODB_USER = 'test'
MONGODB_PASSWD = 'test'

SENTRY_DSN = ''#somethinf about sentry


try:
    from local_conf import *
except ImportError, e:
    pass
except Exception, e:
    logging.warn("Cannot import configurations from local_config, error: %s" % e)

SITE = "http://" + SITE_DOMAIN + ":" + PORT
