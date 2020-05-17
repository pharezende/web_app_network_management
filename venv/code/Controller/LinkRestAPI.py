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
        rows = request.get_json()
        result = link_model.insert_several_rows_in_db(rows)
        return result

    def delete(self):
        return link_model.delete_all()


class Link(Resource):

    def get(self):
        row = request.get_json()
        result = link_model.get_row(row)
        return result

    def post(self):
        row = request.get_json()
        return link_model.insert_row_in_db(row)

    def delete(self):
        row = request.get_json()
        result = link_model.delete_row(row)
        return result

link_model = LinkModel()
