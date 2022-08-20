from flask import Flask, request, jsonify
app = Flask(__name__)
@app.route('/abc', methods=['GET','POST'])
def test():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify((str(result)))

@app.route('/abc1/multiplication', methods=['GET','POST'])
def multiplication1():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a*b
        return jsonify((str(result)))

@app.route('/abc1/division1', methods=['GET','POST'])
def div1():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a/b
        return jsonify((str(result)))

@app.route('/abc1/exponent1', methods=['GET','POST'])
def expo1():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a%b
        return jsonify((str(result)))

@app.route('/abc1/root12', methods=['GET','POST'])
def root1():
    if (request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a**b
        return jsonify((str(result)))


@app.route('/dbconn1', methods=['GET','POST'])
def mysql_dbconn():
    if (request.method=='POST'):
        try:
            engine = conn.connect(host='localhost', user='root', passwd='susant123')
            #establish connection
            cursor = engine.cursor()  # creating cursor object
            query1 = request.json['query_db'] # "query_db" : "create database API_DB"
            cursor.execute(query1)
            result = "database created"
            engine.close()
            return jsonify((str(result)))
        except Exception as e:
            return jsonify((str(e)))

if __name__ == '__main__':
    app.run()