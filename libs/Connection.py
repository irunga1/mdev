import mysql.connector
class Connection:
    mycursor =""
    result = ""
    mydb = ""
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root2",
            passwd="123456JP",
            database="masterdevel"
        )
    def query(self,query, params):
        mycursor = self.mydb.cursor()
        mycursor.execute(query,params)
        self.result = mycursor.fetchall()
        return self.result

    def query2(self,query):
        mycursor = self.mydb.cursor()
        mycursor.execute(query)
        mycursor.commit()
        return "succes"