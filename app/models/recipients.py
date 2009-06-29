# Author: Alex Ksikes 

import web
import config

import MySQLdb, re

# we are forced to use MySQLdb in order to keep the columns order
def __get_cursor():
    param = config.db_records_settings
    return MySQLdb.connect(user=param.user, passwd=param.passwd, db=param.db, use_unicode=True).cursor()

def get(sql_query, offset, limit):
    c = __get_cursor()
    
    c.execute(sql_query + ' limit %s offset %s' % (limit, offset))
    columns = [x[0] for x in c.description]
    results = c.fetchall()
    
    query_count = re.sub('select .*? from', 'select count(*) from', sql_query, re.I)
    c.execute(query_count)
    count = c.fetchall()[0][0]
         
    return (results, count, columns)

def get_all(sql_query):
    db = web.database(**config.db_records_settings)
    return db.query(sql_query)