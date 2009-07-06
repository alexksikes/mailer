# Author: Alex Ksikes 

import web
import config

from config import view
from web import form

from app.models import templates
from app.helpers import utils

sendmail_form = \
    utils.Form(
    form.Textbox('reply_to', 
        description='Reply to: '),
    form.Textbox('to', 
        form.notnull,
        description='To: ',
        pre='<label class="help" for="to">Use the template variable email e.g. $email specified by the SQL query.</label>'),
    form.Textbox('subject', 
        form.notnull,
        description='Subject: ',
        pre='<label class="help" for="to">Use any template variable e.g. $variable_name specified by the SQL query.</label>'),
    form.Textarea('message', 
        form.notnull,
        description='Message: ',
        pre='<label class="help" for="to">Use any template variable e.g. $variable_name specified by the SQL query.</label>'),
    form.Checkbox('send_copy',
        description='',
        post='<span>Send a copy to:</span> <span>%s</span>' % web.htmlquote(config.mail_bcc)),
    form.Checkbox('force_resend',
        description='',
        post='<span>Force resend to previously emailed recipients.</span>'))
    
class index:
    def GET(self):
        return view.base(view.index(view.sendmail_form(sendmail_form())))

class send:    
    def POST(self):
        f = sendmail_form()
        
        count = 0
        if f.validates():
            d = f.d; d.sql_query =  web.input().sql_query
            count = templates.send(d.to, d.subject, d.message, d.sql_query, d.reply_to, d.send_copy)
        return view.sendmail_form(f, success=f.valid, count=count)