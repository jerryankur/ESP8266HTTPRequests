from flask import Flask, jsonify, request
app=Flask(__name__)
alldata=['ankur']
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
		alldata.append(data)
		return data
if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000)   #host is what type of connection and what should accept , 0.0.0.0 means it can accept every connections
print('Exited')