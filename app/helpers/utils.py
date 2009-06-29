# Author: Alex Ksikes 

import web
import config

import md5, time, types

def dict_remove(d, *keys):
    for k in keys:
        if d.has_key(k):
            del d[k]

def make_unique_md5():
    return md5.md5(time.ctime() + config.encryption_key).hexdigest()

def get_all_functions(module):
    functions = {}
    for f in [module.__dict__.get(a) for a in dir(module)
        if isinstance(module.__dict__.get(a), types.FunctionType)]:
        functions[f.__name__] = f
    return functions

def sqlands(left, lst):
    """Similar to webpy sqlors but for ands"""
    if isinstance(lst, web.utils.iters):
        lst = list(lst)
        ln = len(lst)
        if ln == 0:
            return web.SQLQuery("1!=2")
        if ln == 1:
            lst = lst[0]
    if isinstance(lst, web.utils.iters):
        return web.SQLQuery(['('] +
          sum([[left, web.sqlparam(x), ' AND '] for x in lst], []) +
          ['1!=2)']
        )
    else:
        return left + web.sqlparam(lst)

def get_ip():
    return web.ctx.get('ip', '000.000.000.000')

class Form(web.form.Form):
   def render_css(self):
        out = []
        out.append(self.rendernote(self.note))
        for i in self.inputs:
            if i.note:
                out.append('<div class="wrong" id="box_%s">' % i.id)
            else:
                out.append('<div id="box_%s">' % i.id)
            out.append('<label for="%s">%s</label>' % (i.id, web.websafe(i.description)))
            out.append(i.pre)
            out.append(i.render())
            out.append(i.post)
            out.append('</div>\n')
        return ''.join(out)    