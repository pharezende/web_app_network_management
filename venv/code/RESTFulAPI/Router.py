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
        rows = []
        for key in routers_hash_map:
            #Return to the Client the way I want
            row = routers_hash_map[key]
            rows.append(row.get_json())
        return rows

    def post(self):
        rows = request.get_json()
        router_model.insert_several_db(rows)


class Router(Resource):

    def get(self):
        row = request.get_json()
        attribute = router_model.get_attribute_for_matching()
        value = row[attribute]
        identifier = router_model.hash_function(value)
        if identifier in routers_hash_map:
            router = routers_hash_map[identifier]
            #Return to the Client the way I want
            return "Name:" + router.get_name() + ", Number of Interfaces:" + str(router.get_number_interfaces())
        else:
            return "Invalid Name"

    def post(self):
        router_row = request.get_json()
        router_model.insert_db(router_row)

    def delete(self):
        row = request.get_json()
        attribute = router_model.get_attribute_for_matching()
        value = row[attribute]
        identifier = router_model.hash_function(value)
        if identifier in routers_hash_map:
            router_model.delete_row_db(identifier)
            return "OK!"
        else:
            return "Invalid Name"

router_model = RouterModel()
routers_hash_map = router_model.get_router_hash_map()

