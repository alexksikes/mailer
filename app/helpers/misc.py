# Author: Alex Ksikes

import web
import config

import re, urlparse, datetime, urllib, utils, string

def format_date(d, f):
    return d.strftime(f)

def url_quote(url):
    return web.urlquote(url)

def html_quote(html):
    return web.htmlquote(url)

def url_encode(query, clean=True, doseq=True, **kw):
    query = web.dictadd(query, kw)
    if clean is True:
        for q, v in query.items():
            if not v:
                del query[q]
    return urllib.urlencode(query, doseq)

def cut_length(s, max=40):
    if len(s) > max:
        s = s[0:max] + '...'
    return s

def get_nice_url(url):
    host, path = urlparse.urlparse(url)[1:3]
    if path == '/':
        path = ''
    return cut_length(host+path)

def capitalize_first(str):
    if not str:
        str = ''
    return ' '.join(map(string.capitalize, str.lower().split()))

def text2html(s):
    s = replace_breaks(s)
    s = replace_indents(s)
    return replace_links(s)
    
def replace_breaks(s):
    return re.sub('\n', '<br />', s)

def replace_indents(s):
    s = re.sub('\t', 4*' ', s)
    return re.sub('\s{2}', '&nbsp;'*2, s)

def replace_links(s):
    return re.sub('(http://[^\s]+)', r'<a rel="nofollow" href="\1">' + get_nice_url(r'\1') + '</a>', s, re.I)

# we may need to get months ago as well
def how_long(d):
    return web.datestr(d, datetime.datetime.now())

def split(pattern, str):
    return re.split(pattern, str)

def get_site_config(attr):
    return getattr(config, attr)
