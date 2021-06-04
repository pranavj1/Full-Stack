from flask import Flask, request, jsonify
import mysql.connector as conn
app = Flask(__name__)
@app.route('/tblcreation/SQL', methods=['POST'])
def create_SQL():
    if (request.method=="POST"):
        host=request.json['host']
        user=request.json['user']
        passw=request.json['passw']
        tbl_name=request.json['tbl_name']
        c1=request.json['c1']
        c2=request.json['c2']
        c3=request.json['c3']
        t1=request.json['t1']
        t2=request.json['t2']
        t3=request.json['t4']
        try:
            mydb = conn.connect(host=host,database="abc", user=user, passwd=passw, use_pure=True)
            return jsonify("conn established")
            cur = mydb.cursor()
            query="create table {} ({} {},{} {},{} {})".format(tbl_name,c1,t1,c2,t2,c3,t3)
            cur.execute(query)
            mydb.close()
            return jsonify("tble created")
        except Exception as e:
            mydb.close()
            return jsonify("error occured\n"+str(e))

@app.route('/Insert_1/SQL', methods=['POST'])
def Inser1_SQL():
    if (request.method=="POST"):
        host = request.json['host']
        user = request.json['user']
        passw = request.json['passw']
        tbl_name = request.json['tbl_name']
        c1 = request.json['c1']
        c2 = request.json['c2']
        c3 = request.json['c3']
        try:
            mydb = conn.connect(host=host,database="abc", user=user, passwd=passw)
            cur = mydb.cursor()
            #query="Insert INTO xyz(Name,ID,comp) VALUE({},{},{})".format(c1,c2,c3)
            #cur.execute(query)
            cur.execute("Insert INTO xyz(Name,ID,comp) VALUE(%s, %s, %s)",(c1,c2,c3))
            mydb.commit()
            mydb.close()
            return jsonify("Data added")
        except Exception as e:
            mydb.close()
            return jsonify("error occured\n"+str(e))
@app.route('/Insert_m/SQL', methods=['POST'])
def Inserm_SQL():
    if (request.method=="POST"):
        host = request.json['host']
        user = request.json['user']
        passw = request.json['passw']
        tbl_name = request.json['tbl_name']
        c1 = request.json['c1']
        c2 = request.json['c2']
        c3 = request.json['c3']
        c4 = request.json['c4']
        c5 = request.json['c5']
        c6 = request.json['c6']
        try:
            mydb = conn.connect(host=host,database="abc", user=user, passwd=passw)
            cur = mydb.cursor()
            #query="Insert INTO xyz(Name,ID,comp) VALUES({},{},{}),({},{},{})".format(c1,c2,c3,c4,c5,c6)
            #cur.execute(query)
            cur.execute("Insert INTO xyz(Name,ID,comp) VALUES(%s, %s, %s),(%s, %s, %s)",(c1,c2,c3,c4,c5,c6))
            mydb.commit()
            mydb.close()
            return jsonify("Data added")
        except Exception as e:
            mydb.close()
            return jsonify("error occured\n"+str(e))

@app.route('/update/SQL', methods=['POST'])
def Update_SQL():
    if (request.method=="POST"):
        host=request.json['host']
        user=request.json['user']
        passw=request.json['passw']
        tbl_name=request.json['tbl_name']
        c1=request.json['c1']
        c2=request.json['c2']
        c3=request.json['c3']
        try:
            mydb = conn.connect(host=host,database="abc", user=user, passwd=passw, use_pure=True)
            cur = mydb.cursor()
            #query="UPDATE %s SET ID=%s,comp=%s WHERE Name=%s",(tbl_name,c2,c3,c1)
            cur.execute("UPDATE xyz SET ID=%s,comp=%s WHERE Name=%s",(c2,c3,c1))
            mydb.commit()
            mydb.close()
            return jsonify("tble updated")
        except Exception as e:
            mydb.close()
            return jsonify("error occured\n"+str(e))

@app.route('/delete/SQL', methods=['POST'])
def Delete_SQL():
    if (request.method=="POST"):
        host=request.json['host']
        user=request.json['user']
        passw=request.json['passw']
        tbl_name=request.json['tbl_name']
        c1=request.json['c1']
        c2 = request.json['c2']
        try:
            mydb = conn.connect(host=host,database="abc", user=user, passwd=passw, use_pure=True)
            cur = mydb.cursor()
            cur.execute("DELETE FROM xyz WHERE Name = %s and ID = %s ",(c1,c2))
            mydb.commit()
            mydb.close()
            return jsonify("mentioned record deleted")
        except Exception as e:
            mydb.close()
            return jsonify("error occured\n"+str(e))

if __name__ == '__main__':
    app.run()