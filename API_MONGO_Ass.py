from flask import Flask, request, jsonify
import pymongo
app = Flask(__name__)
@app.route('/tblcreation/MONGO', methods=['POST'])
def create_Mt():
    if (request.method=="POST"):
        link = request.json['link']  # mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false
        db = request.json['db']
        c_name = request.json['c_name']
        try:
            conn=pymongo.MongoClient(link)
            conn[db]
            db[c_name]
            return jsonify("Collection created")
        except Exception as e:
            return jsonify("error occured\n" + str(e))

@app.route('/Insert_1/MONGO', methods=['POST'])
def create_MI_1():
    if (request.method=="POST"):
        link = request.json['link']  # mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false
        db = request.json['db']
        c_name = request.json['c_name']
        record = request.json['record']
        try:
            conn=pymongo.MongoClient(link)
            Db=conn[db]
            coll=Db[c_name]
            coll.insert_one(record)
            return jsonify("record added")
        except Exception as e:
            return jsonify("error occured\n" + str(e))

@app.route('/Insert_m/MONGO', methods=['POST'])
def create_MI_m():
    if (request.method=="POST"):
        link = request.json['link']  # mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false
        db = request.json['db']
        c_name = request.json['c_name']
        record = request.json['record']
        try:
            conn=pymongo.MongoClient(link)
            Db=conn[db]
            coll=Db[c_name]
            coll.insert_many(record)
            return jsonify("record added")
        except Exception as e:
            return jsonify("error occured\n" + str(e))

@app.route('/Update/MONGO', methods=['POST'])
def Update_M():
    if (request.method=="POST"):
        link = request.json['link']  # mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false
        db = request.json['db']
        id=request.json["id"]
        c_name = request.json['c_name']
        record = request.json['record']
        new_reco = request .json['new_reco']
        try:
            conn=pymongo.MongoClient(link)
            Db=conn[db]
            coll=Db[c_name]
            coll.update_one(record,new_reco)
            return jsonify("record added")
        except Exception as e:
            return jsonify("error occured\n" + str(e))

@app.route('/download/MONGO', methods=['POST'])
def download_M():
    if (request.method=="POST"):
        link = request.json['link']  # mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false
        db = request.json['db']
        c_name = request.json['c_name']
        try:
            conn=pymongo.MongoClient(link)
            Db=conn[db]
            coll=Db[c_name]
            a=coll.find()
            str=""
            for i in a:
                str=str + str(i)
            return jsonify(str)
        except Exception as e:
            return jsonify("error occured\n" + str(e))
if __name__ == '__main__':
    app.run()



