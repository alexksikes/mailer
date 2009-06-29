# Author: Alex Ksikes 

import web
import config

from config import view

from app.helpers import paging
from app.models import recipients

import re

results_per_page = 15

class browse:
    def GET(self):
        i = web.input(start=0, sql_query='')
        start = int(i.start)
        
        results, count, columns = recipients.get(i.sql_query, offset=start, limit=results_per_page)
        pager = web.storage(paging.get_paging(start, count, 
            results_per_page=results_per_page, window_size=1))
        
        return view.recipients_preview(results, columns, pager, i)
