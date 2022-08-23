from flask import Flask, request, jsonify
import pymongo

app = Flask('__name__')  # creating app in Flask() method
#database connection
client = pymongo.MongoClient("mongodb+srv://susant:susant123@cluster0.8beoc.mongodb.net/?retryWrites=true&w=majority")
database=client['api_db1']
collection = database['login_info']

@app.route('/mongo/insert', methods = ['POST'])
def insert1():
    if request.menthod == 'POST':
        name1 = request.json['name']
        num1 = request.json['num']
        collection.insert_one({name1:num1})
        return jsonify(str("inserted one record"))

if __name__ == '__main__':
    app.run(port=5001)
