#!/usr/bin/env python
# Author: Alex Ksikes 

import web
import config
import app.controllers

urls = (
    '/',                                         'app.controllers.handle_templates.index',
    '/send',                                     'app.controllers.handle_templates.send',
    '/recipients',                               'app.controllers.preview_recipients.browse',

    '/(?:img|js|css)/.*',                        'app.controllers.public.public',
)

app = web.application(urls, globals())
if web.config.email_errors:
    app.internalerror = web.emailerrors(web.config.email_errors, web.webapi._InternalError)

if __name__ == "__main__":
    app.run()
