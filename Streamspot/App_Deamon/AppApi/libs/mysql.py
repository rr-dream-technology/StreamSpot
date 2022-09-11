import mysql.connector as mcdb




conn = mcdb.connect(host="mydatabase-1.cmosw4rexij7.us-east-1.rds.amazonaws.com", user="rr3343500", passwd="Rr3343500", database='StreamSpot')
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