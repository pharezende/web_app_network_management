from flask import Flask, request
from flask_restful import Resource, Api
import json
from RouterRestAPI import *
from SwitchRestAPI import *
from HostRestAPI import *
from LinkRestAPI import *
from flask_cors import CORS


if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    cors = CORS(app)

    #Routers API
    api.add_resource(Router, '/routers/single/', '/routers/single/<value>')
    api.add_resource(Routers, '/routers/all/')
    #Switches API
    api.add_resource(Switch, '/switches/single/', '/switches/single/<value>')
    api.add_resource(Switches, '/switches/all/')
    #Hosts API
    api.add_resource(Host, '/hosts/single/', '/hosts/single/<value>')
    api.add_resource(Hosts, '/hosts/all/')
    #Links API
    api.add_resource(Link, '/links/single/', '/links/single/<value_1>/<value_2>')
    api.add_resource(Links, '/links/all/')

    app.run(debug=True)