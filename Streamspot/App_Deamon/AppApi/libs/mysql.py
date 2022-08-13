import mysql.connector as mcdb




conn = mcdb.connect(host="localhost", user="root", passwd="", database='StreamSpot')
cur = conn.cursor()


def Select(Query):
    cur.execute(Query)
    data = cur.fetchall()
    row_headers=[x[0] for x in cur.description]
    json_data=[]
    for result in data:
        json_data.append(dict(zip(row_headers,result)))
    return json_data


def insertData(Query):
    cur.execute(Query)
    conn.commit()
    data = cur.lastrowid
    return data