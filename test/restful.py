from flask import Flask, jsonify, request
app = Flask(__name__)

sensors = [{'name' : 'DHT11', 'value' : 'Temp=22.0C Humidity=35.0%'}, {'name' : 'LDR', 'value' : 'lights ON'}]

@app.route('/sensor', methods=['GET'])
def returnAll():
    return jsonify({'sensors' : sensors})

@app.route('/sensor/<string:name>', methods=['GET'])
def returnOne(name):
    sens = [sensor for sensor in sensors if sensor['name'] == name]
    return jsonify({'sensor' : sensors[0]})

@app.route('/sensor', methods=['POST'])
def addOne():
    sensor = {'name' : request.json['name']}

    sensors.append(sensor)
    return jsonify({'sensors' : sensors})

@app.route('/sensor/<string:name>', methods=['PUT'])
def editOne(name):
    sens = [sensor for sensor in sensors if sensor['name'] == name]
    sens[0]['name'] = request.json['name']
    return jsonify({'sensor' : sens[0]})

if __name__ == '__main__':
    app.run(debug=True, port=8080)