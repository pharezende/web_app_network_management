import json
from Models.CommonDBMethods import DB

class Router():

    def  __init__(self, name, number_interfaces, manufacturer, id):
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
        router_json = {}
        router_json['name'] = self.__name
        router_json['numberOfInterfaces'] = self.__number_interfaces
        router_json['manufacturer'] = self.__manufacturer
        router_json['id'] = self.__id
        return router_json


class RouterModel():

    def __init__(self):
        self.file_name = "/home/pedro/PycharmProjects/flask-intro/venv/code/Database/routers.json"
        self.routers_hash_map = {}
        self.db = DB()
        self.populate_objects()

    def get_router_hash_map(self):
        return self.routers_hash_map

    def populate_objects(self):
        rows = self.db.query_db(self.file_name)
        for row in rows:
            router = Router(row['name'], row['numberOfInterfaces'], row['manufacturer'], row['id'])
            self.routers_hash_map[router.get_id()] = router

    def insert_db(self, row):
        rows = []
        row['id'] = self.hash_function(row[self.get_attribute_for_matching()])
        router = Router(row['name'], row['numberOfInterfaces'], row['manufacturer'], row['id'])
        self.routers_hash_map[router.get_id()] = router
        for key in self.routers_hash_map:
            row = self.routers_hash_map[key]
            rows.append(row.get_json())
        self.db.update_db(self.file_name, rows)

    def insert_several_db(self, rows):
        rows_to_insert_in_db = []
        for row in rows:
            row['id'] = self.hash_function(row[self.get_attribute_for_matching()])
            router = Router(row['name'], row['numberOfInterfaces'], row['manufacturer'], row['id'])
            self.routers_hash_map[router.get_id()] = router
        for key in self.routers_hash_map:
            value = self.routers_hash_map[key]
            rows_to_insert_in_db.append(value.get_json())
        self.db.update_db(self.file_name, rows_to_insert_in_db)

    def delete_row_db(self, id):
        del self.routers_hash_map[id]
        rows = self.routers_hash_map
        with open(self.file_name, 'w') as json_file:
            json_list = []
            for key_row in rows:
                json_data = rows[key_row].get_json()
                json_list.append(json_data)
            json.dump(json_list, json_file, indent=4)

    def delete_all(self):
        self.routers_hash_map.clear()
        self.db.clear_db(self.file_name)


    def get_attribute_for_matching(self):
        return 'name'

    def hash_function(self, name):
        return hash(name) % 10000