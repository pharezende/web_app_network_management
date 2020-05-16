from flask import Flask, request
from flask_restful import Resource, Api
import json
from Router import *
from Switch import *

if __name__ == '__main__':

    app = Flask(__name__)
    api = Api(app)

    #Routers API
    api.add_resource(Router, '/routers/single/')
    api.add_resource(Routers, '/routers/all/')
    #Switches API
    api.add_resource(Switch, '/switches/single/')
    api.add_resource(Switches, '/switches/all/')

    app.run(debug=True)