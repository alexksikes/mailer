# Author: Alex Ksikes

import web

from app.helpers import misc
from app.helpers import utils

# connect to the mailer database.
db = web.database(dbn='mysql', db='mailer', user='user', passwd='password')

# in development debug error messages and reloader.
web.config.debug = False

# in develpment template caching is set to false.
cache = True

# global used template functions.
globals = utils.get_all_functions(misc)

# the domain where the site is hosted.
site_domain = 'www.your_domain.com'

# set global base template.
view = web.template.render('app/views', cache=cache,  globals=globals)

# used as a salt.
encryption_key = 'a random string'

# in production the internal errors could be emailed to us.
web.config.email_errors = ''

# email of the sender.
# IMPORTANT: make sure SPF and reverse DNS are setup to avoid mails being marked as spam.
mail_sender = 'Mailer sender name <noreply@example.com>'

# used for the send a copy feature.
mail_bcc = 'Send a copy to name <example@example.com>'

# db setting used to browse through your databases.
# IMPORTANT: make sure user only has select rights.
db_records_settings = web.storage(dbn='mysql', db='mlss', user="user", passwd="password")
