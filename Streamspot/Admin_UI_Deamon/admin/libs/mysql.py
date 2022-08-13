import mysql.connector as mcdb




conn = mcdb.connect(host="localhost", user="root", passwd="", database='StreamSpot')
cur = conn.cursor()


def Select(Query):
    cur.execute(Query)
    data = cur.fetchall()
    return data


def insertData(Query):
    cur.execute(Query)
    data = cur.fetchall()
    return data
    





        



