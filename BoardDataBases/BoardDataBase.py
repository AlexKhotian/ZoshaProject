__author__ = 'Alex'

import sqlite3 as lite

# data defaults enum
successCreate = 1
errorCreate = -1

class BoardDatabase(object):
    def __init__(self):
        pass
    m_dataId = 0

    def createDataBase(self):
        connection = lite.connect('login.db')
        with connection:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS Users(Id INT, Name TEXT, Password Text)")


    def insertDataIntoLoginDatabase(self, name, password):
        connection = lite.connect('login.db')
        with connection:
            cursor = connection.cursor()
            dataset = (self.m_dataId, name, password)
            cursor.execute("INSERT INTO Users VALUES(?,?,?)", dataset)
            self.m_dataId += 1

    def getUserDataFromDB(self, name):
        connection = lite.connect('login.db')
        with connection:
            cursor = connection.cursor()
            cursor.execute("SELECT Password FROM Users WHERE Name = '" + name + "'")
            info = cursor.fetchall()
            return info
