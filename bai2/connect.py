import mysql.connector

def getConnection():
    connection = mysql.connector.connect(host='localhost',
                                        user='root',
                                        passwd='root',
                                        database='Quan_ly_nhan_vien')

    return connection