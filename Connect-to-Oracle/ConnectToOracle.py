#!/usr/bin/env python
import cx_Oracle
import os
os.environ["PYTHONIOENCODING"] = "utf-8"
# Load Procedure File:
ProcedureFile = open('procedure.sql')
CallProcedure = ProcedureFile.read()
ProcedureQueries = CallProcedure.replace('\n', '').split(';')[:-1]
# Connect to Oracle DB
Connection_String = u'myuser/Oracle123@192.168.11.41:1521/mydb'
Connection = cx_Oracle.connect(Connection_String)
Cursor = Connection.cursor()
# Execute Query Data File
for i in ProcedureQueries:
   Cursor.execute(i)