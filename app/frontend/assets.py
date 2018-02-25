# -*- coding: utf-8 -*-
"""
    riskmanager.frontend.assets
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    frontend application asset "pipeline"
"""

from flask_assets import Environment, Bundle


js_build = Bundle("*.js", output="build.js")


def init_app(app):
    webassets = Environment(app)
    webassets.register('js_build', js_build)
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug
