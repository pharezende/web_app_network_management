import json
from Models.CommonDBMethods import DB

class Switch():

    def __init__(self, name, number_interfaces, manufacturer, id):
        self.__name = name
        self.__number_interfaces = number_interfaces
        self.__manufacturer = manufacturer
        self.__id = id

    def get_name(self):
        return self.__name

    def get_number_interfaces(self):
        return self.__number_interfaces

    def get_manufacturer(self):
        return self.__manufacturer

    def get_id(self):
        return self.__id

    def get_json(self):
        switch_json = {}
        switch_json['name'] = self.__name
        switch_json['numberOfInterfaces'] = self.__number_interfaces
        switch_json['manufacturer'] = self.__manufacturer
        switch_json['id'] = self.__id
        return switch_json

class SwitchModel():

    def __init__(self):
        self.file_name = "/home/pedro/PycharmProjects/flask-intro/venv/code/Database/switches.json"
        self.switches_hash_map = {}
        self.db = DB()
        self.set_switches_hash_map()

    def get_file_name(self):
        return self.file_name

    def get_switches_hash_map(self):
        return self.switches_hash_map

    def set_switches_hash_map(self):
        rows = self.db.query_db(self.file_name)
        for row in rows:
            switch = Switch(row['name'], row['numberOfInterfaces'], row['manufacturer'], row['id'])
            self.switches_hash_map[switch.get_id()] = switch


    def insert_several_db(self, rows):
        rows_db = self.db.query_db(self.file_name)
        for row in rows:
            row['id'] = self.hash_function(row['name'])
            switch = Switch(row['name'], row['numberOfInterfaces'], row['manufacturer'], row['id'])
            self.switches_hash_map[switch.get_id()] = switch
            rows_db.append(row)
        self.db.update_db(self.file_name, rows_db)

    def insert_db(self, row):
        rows = self.db.query_db(self.file_name)
        row['id'] = self.hash_function(row['name'])
        switch = Switch(row['name'], row['numberOfInterfaces'], row['manufacturer'], row['id'])
        self.switches_hash_map[switch.get_id()] = switch
        rows.append(row)
        self.db.update_db(self.file_name, rows)

    def delete_row_db(self, id):
        del self.switches_hash_map[id]
        rows = self.switches_hash_map
        with open(self.file_name, 'w') as json_file:
            json_list = []
            for key_row in rows:
                json_data = rows[key_row].get_json()
                json_list.append(json_data)
            json.dump(json_list, json_file, indent=4)

    def get_attribute_for_matching(self):
        return 'name'

    def hash_function(self, name):
        return hash(name) % 10000



