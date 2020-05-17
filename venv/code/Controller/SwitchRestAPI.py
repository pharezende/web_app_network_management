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
        return switch_model.get_rows()

    def post(self):
        rows = request.get_json()
        switch_model.insert_several_db(rows)

    def delete(self):
        switch_model.delete_all()

class Switch(Resource):

    def get(self):
        object = request.get_json()
        return switch_model.get_row(object)

    def post(self):
        row = request.get_json()
        switch_model.insert_db(row)

    def delete(self):
        object = request.get_json()
        switch_model.delete_row_db(object)


switch_model = SwitchModel()



