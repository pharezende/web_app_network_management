from flask import request
from flask_restful import Resource
import os
import sys
sys.path.append(os.path.realpath('..')) #Change the dir to import my modules. It will not work, otherwise
from Models.LinkModel import *
import json

os.environ["PYTHONHASHSEED"] = "0"

class Links(Resource):

    def get(self):
        result = link_model.get_rows()
        return result

    def post(self):
        objects = request.get_json()
        result = link_model.insert_several_rows_in_db(objects)
        return result

    def delete(self):
        return link_model.delete_all()


class Link(Resource):

    def get(self, value_1, value_2):
        result = link_model.get_row(value_1, value_2)
        return result

    def post(self):
        object = request.get_json()
        return link_model.insert_row_in_db(object)

    def delete(self):
        object = request.get_json()
        result = link_model.delete_row(object)
        return result

link_model = LinkModel()
