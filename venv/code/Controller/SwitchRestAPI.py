from flask import request
from flask_restful import Resource
import os
import sys
sys.path.append(os.path.realpath('..')) #Change the dir to import my modules. It will not work, otherwise
from Models.SwitchModel import SwitchModel, Switch
import json

os.environ["PYTHONHASHSEED"] = "0"

class Switches(Resource):

    def get(self):
        rows = []
        for key in switches_hash_map:
            # Return to the Client the way I want
            row = switches_hash_map[key]
            rows.append(row.get_json())
        return rows

    def post(self):
        rows = request.get_json()
        switch_model.insert_several_db(rows)

    def delete(self):
        switch_model.delete_all()

class Switch(Resource):

    def get(self):
        row = request.get_json()
        attribute = switch_model.get_attribute_for_matching()
        value = row[attribute]
        identifier = switch_model.hash_function(value)
        if identifier in switches_hash_map:
            switch = switches_hash_map[identifier]
            return switch.get_json()
        else:
            return "Invalid Name"

    def post(self):
        row = request.get_json()
        switch_model.insert_db(row)

    def delete(self):
        row = request.get_json()
        attribute = switch_model.get_attribute_for_matching()
        value = row[attribute]
        identifier = switch_model.hash_function(value)
        if identifier in switches_hash_map:
            switch_model.delete_row_db(identifier)
            return "OK!"
        else:
            return "Invalid Name"


switch_model = SwitchModel()
switches_hash_map = switch_model.get_switches_hash_map()



