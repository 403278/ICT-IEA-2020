from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Dht11(Resource):
    def get(self):
        return {'name' : 'DHT11', 'value' : 'Temp=22.0C Humidity=35.0%'}
    
class Ldr(Resource):
    def get(self):
        return {'name' : 'LDR', 'value' : 'lights ON'}


api.add_resource(Dht11, '/dht11')
api.add_resource(Ldr, '/ldr')


if __name__ == '__main__':
    app.run(debug=True)
