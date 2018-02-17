# -*- coding: utf-8 -*-
"""
    riskmanager.frontend.assets
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    frontend application asset "pipeline"
"""

from flask_assets import Environment, Bundle


#: consolidated css bundle
css_all = Bundle("css/bootstrap.min.css", "css/risk_manager.css",
                 "css/bootstrap-responsive.min.css",
                 filters="cssmin", output="css/risk_manager.min.css")

#: vendor js bundle
js_vendor = Bundle("js/vendor/jquery-1.10.1.min.js",
                   "js/vendor/bootstrap-2.3.3.min.js",
                   "js/vendor/underscore-1.4.4.min.js",
                   filters="jsmin", output="js/vendor.min.js")

#: application js bundle
js_main = Bundle("js/*.js", filters="jsmin", output="js/main.min.js")


def init_app(app):
    webassets = Environment(app)
    webassets.register('css_all', css_all)
    webassets.register('js_vendor', js_vendor)
    webassets.register('js_main', js_main)
    webassets.manifest = 'cache' if not app.debug else False
    webassets.cache = not app.debug
    webassets.debug = app.debug
