from flask import Flask, jsonify, request
from pymongo import MongoClient
import time
app=Flask(__name__)
client=MongoClient('localhost',27017)
db=client.iotdb
alldata=[]
@app.route('/')
def hello():
	print ('hello() function called')
	return 'Hello'
@app.route('/data',methods=['GET','POST'])
def data():
	print('data() function called')
	if request.method == 'GET':
		return jsonify(alldata)
	elif request.method == 'POST':
		data =request.json
		data["_id"]="pkt_"+str(time.time())
		result=db.mydatacollection.insert_one(data)
		alldata.append(data)
		print(data)
		return jsonify(data)
if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000)   #host is what type of connection and what should accept , 0.0.0.0 means it can accept every connections
print('Exited')
