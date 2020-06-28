
from flask import Flask, render_template, jsonify ,request
from pymongo import MongoClient
import os

app = Flask(__name__)
client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],27017
)
db = client.PersonDB
person = db.person


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/api/person/get_all',methods=['GET'])
def getAllStudents():
    # person.insert_one({
    #     "first_name" : "Donnukrit",
    #     "last_name" : "Satirakul"
    # })
    return jsonify({"msg":"Hello World2"})
@app.route('/api/person/add',methods=['POST'])
def add_new():
    data = request.get_json()
    _person = {
        'first_name' : data['first_name'],
        'last_name' : data['last_name'],
        'faculty' : data['faculty'],
        'major' : data['major'],
        'home' : data['home']
    }
    person.insert_one(_person)
    return jsonify(data ,{'msg' : 'Complete'})
if __name__ == '__main__':
  app.run(host='0.0.0.0',debug=True)
 