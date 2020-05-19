from flask import request
from flask_restful import Resource
import os
import sys
sys.path.append(os.path.realpath('..')) #Change the dir to import my modules. It will not work, otherwise
from Models.HostModel import HostModel, Host
import json

os.environ["PYTHONHASHSEED"] = "0"

class Hosts(Resource):

    def get(self):
        return host_model.get_rows()

    def post(self):
        objects = request.get_json()
        host_model.insert_rows_in_db(objects)

    def delete(self):
        host_model.delete_all()

class Host(Resource):

    def get(self, value):
        return host_model.get_row(value)

    def post(self):
        object = request.get_json()
        host_model.insert_row_in_db(object)

    def delete(self):
        object = request.get_json()
        host_model.delete_row_db(object)

host_model = HostModel()


