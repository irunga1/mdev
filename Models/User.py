from sqlobject import *
import mysql.connector
sqlhub.processConnection = connectionForURI("mysql://root2:123456JP@localhost/masterdevel")

class User(SQLObject):
    id = IntCol()
    name = StringCol(length=100)
    email = StringCol(length=100)
    password = StringCol(length=100)
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password = password
