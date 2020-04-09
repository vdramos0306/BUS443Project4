# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 23:21:48 2020

@author: Vernonica
"""

from pip._internal import main
main(['install','mysql-connector-python-rf'])

import mysql.connector as mysql

mydb = mysql.connect(
        host ='localhost', user ='veronica', passwd = 'Hahokay123.', database = 'bus443_project4')

cursor = mydb.cursor()

cursor.execute("INSERT INTO faculty (firstname, lastname, coursename, courselocation) VALUES ('Veronica', 'Ramos', 'BUS443', '0023');")
cursor.execute( "SELECT*FROM faculty;")

data = cursor.fetchall()

print(data)


