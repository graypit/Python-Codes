#!/usr/bin/python2
import pyodbc
import sys
# Set Encoding:
reload(sys)
sys.setdefaultencoding('UTF8')
# SQL Variables:
DB_IP = '192.168.1.44'
DB_PORT = '1433'
DB_NAME = 'TestDB'
DB_USER = 'dbuser'
DB_PASS = 'dbpass123'
# Set Connection Strings:
Connect = pyodbc.connect('DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(
'ODBC Driver 13 for SQL Server',DB_IP + ',' + DB_PORT,DB_NAME,DB_USER,DB_PASS))
Cursor = Connect.cursor()
Cursor.execute('select  * from Sales')
File= open("./output-data.sql","w+")
for data in Cursor:
    File.write("insert into Sales values ('")
    for row in range(33):
        if row !=32:
            File.write(str(data[row]).replace("\n", '') + "','")
        else:
            File.write(str(data[row]).replace("\n", ''))
    File.write("');\n")
File.write('commit;')
File.close()