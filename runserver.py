# -*- coding: utf-8 -*-

from projectname.app import app


if(__name__ == "__main__"):
    app.debug = app.config["DEBUG_MODE"]
    app.run(host='0.0.0.0')
