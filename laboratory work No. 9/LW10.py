from datetime import datetime

from flask import Flask
from flask import request
from pymongo import MongoClient
from bson.json_util import dumps
import json
from flask import jsonify


client = MongoClient('mongodb://localhost:27017')
db = client.schedule
print(db)
app = Flask(__name__)

@app.route("/add_lessons", methods = ['POST'])
def add_lessons():
    try:
        data = json.loads(request.data)
        idl = data['ID']
        day = data['DayOfWeek']
        st = datetime.strptime(data['Start_Time'], '%Y-%m-%dT%H:%M:%S.%f%z')
        et = datetime.strptime(data['EndTime'], '%Y-%m-%dT%H:%M:%S.%f%z')
        idroom = data['ClassroomID']
        idgroup = data['GroupID']
        iddiscipline = data['DisciplineID']
        idteacher = data['TeacherID']
        if idl and day and st and et and idroom and idgroup and iddiscipline and idteacher:
            status = db.lessons.insert_one({'ID':idl, 'DayOfWeek' : day,'Start_Time':st,'EndTime':et, 'ClassroomID': idroom, 'GroupID': idgroup, 'DisciplineID': iddiscipline, 'TeacherID': idteacher})
        return dumps({'message' : 'Пара добавлена'}, ensure_ascii=False)
    except Exception as e:
        return dumps({'error' : str(e)})
@app.route("/lessons", methods = ['GET'])
def lessons():
    try:
        product = db.lessons.find()
        resp = dumps(product, ensure_ascii=False)
        return resp
    except Exception as e:
        return dumps({'error' : str(e)})

@app.route("/get_group_schedule/<group_id>", methods=['GET'])
def get_group_schedule(group_id):
    try:
        shedule_g = db.lessons.find({'GroupID': group_id})
        resp = jsonify([lesson for lesson in shedule_g])
        # resp = dumps(shedule_g, ensure_ascii=False)
        return resp
    except Exception as e:
        return dumps({'error' : str(e)})

@app.route("/delete_lessons/<id>", methods = ['DELETE'])
def delete_lessons(id):
    try:
        db.lessons.delete_one({'ID': id})
        resp = dumps({'message' : 'Пара удалена'}, ensure_ascii=False)
        return resp
    except Exception as e:
        return dumps({'error' : str(e)})

@app.route("/change_teacher", methods = ['PUT'])
def change_teacher():
    try:
        data = json.loads(request.data)
        idl = data['ID']
        TeacherID = data['TeacherID']
        db.lessons.update_one({'ID': idl}, {'$set': {'TeacherID': TeacherID}})
        resp = dumps({'message' : 'Преподаватель изменен'}, ensure_ascii=False)
        return resp
    except Exception as e:
        return dumps({'error' : str(e)})

if __name__ == "__main__":
    app.run(debug=True)