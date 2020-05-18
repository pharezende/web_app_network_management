from flask import request
from flask_restful import Resource
import os
import sys
sys.path.append(os.path.realpath('..')) #Change the dir to import my modules. It will not work, otherwise
from Models.RouterModel import RouterModel, Router
import json

os.environ["PYTHONHASHSEED"] = "0"

class Routers(Resource):

    def get(self):
        result = router_model.get_rows()
        return result

    def post(self):
        objects = request.get_json()
        router_model.insert_several_db(objects)

    def delete(self):
        router_model.delete_all()



class Router(Resource):

    def get(self, value):
        result = router_model.get_row(value)
        return result

    def post(self):
        router_row = request.get_json()
        router_model.insert_db(router_row)

    def delete(self):
        object = request.get_json()
        result = router_model.delete_row_db(object)
        return result

router_model = RouterModel()

