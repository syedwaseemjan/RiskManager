# -*- coding: utf-8 -*-
"""
    app.settings
    ~~~~~~~~~~~~~~~

    riskmanager settings module
"""
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DEBUG = False
SQLALCHEMY_ECHO = False
WTF_CSRF_ENABLED = False
SECRET_KEY = 'super-secret-key'
SQLALCHEMY_DATABASE_URI = "manager_risk.db"
