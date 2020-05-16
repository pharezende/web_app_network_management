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
        rows = []
        for key in hosts_hash_map:
            row = hosts_hash_map[key]
            rows.append(row.get_json())
        return rows

    def post(self):
        rows = request.get_json()
        host_model.insert_rows_in_db(rows)

    def delete(self):
        host_model.delete_all()

class Host(Resource):

    def get(self):
        row = request.get_json()
        attribute = host_model.get_attribute_for_matching()
        value = row[attribute]
        identifier = host_model.hash_function(value)
        if identifier in hosts_hash_map:
            host = hosts_hash_map[identifier]
            return host.get_json()
        else:
            return "Invalid Name"

    def post(self):
        row = request.get_json()
        host_model.insert_row_in_db(row)

    def delete(self):
        row = request.get_json()
        attribute = host_model.get_attribute_for_matching()
        value = row[attribute]
        identifier = host_model.hash_function(value)
        if identifier in hosts_hash_map:
            host_model.delete_row_db(identifier)
            return "OK!"
        else:
            return "Invalid Name"

host_model = HostModel()
hosts_hash_map = host_model.get_hosts_hash_map()


