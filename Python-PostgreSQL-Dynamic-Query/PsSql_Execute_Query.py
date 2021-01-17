#!/usr/bin/python
# Author: Habib Guliyev 12.17.2020
# Import Libraries:
#from __future__ import print_function
import psycopg2
import datetime as date
from jinja2 import Template
# Global Variables:
QueryFilename = 'query.sql'
# PGSQL Connection string:
hostname = '192.168.1.55'
username = 'admin'
password = 'superstrongpass'
database = 'postgres'
# Get Date and Set to Correct Structure:
TodayDate = date.datetime.now()
SevenDayBeforeDate = TodayDate - date.timedelta(days=7)
WhereDate = TodayDate.strftime("%Y-%m-%d ") + '23:59:59'
FromDate = SevenDayBeforeDate.strftime("%Y-%m-%d ") + '00:00:00'
# Do Jinja Template Magic:
with open(QueryFilename) as file_:
    template = Template(file_.read())
Query = template.render(wheredate=WhereDate,fromdate=FromDate)
# Execute Query Function:
def ExecuteQuery( conn ) :
    cur = conn.cursor()
    cur.execute(Query)
    print("Updated:")
    print(cur.rowcount)
# Connect/Prepare PGSQL
myConnection = psycopg2.connect( host=hostname, user=username, password=password, dbname=database )
ExecuteQuery( myConnection )
myConnection.close()