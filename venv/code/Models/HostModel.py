import json
from Models.CommonDBMethods import DB

class Host:

    def __init__(self, name, number_of_interfaces, id):
        self.__name = name
        self.__number_of_interfaces = number_of_interfaces
        self.__id = id

    def get_name(self):
        return self.__name

    def get_number_of_interfaces(self):
        return self.__number_of_interfaces()

    def get_id(self):
        return self.__id

    def get_json(self):
        host_json = {}
        host_json['name'] = self.__name
        host_json['numberOfInterfaces'] = self.__number_of_interfaces
        host_json['id'] = self.__id
        return host_json

class HostModel:

    def __init__(self):
        self.file_name = "/home/pedro/PycharmProjects/flask-intro/venv/code/Database/hosts.json"
        self.hosts_hash_map = {}
        self.db = DB()
        self.set_hosts_hash_map()

    def get_hosts_hash_map(self):
        return self.hosts_hash_map

    def set_hosts_hash_map(self):
        rows = self.db.query_db(self.file_name)
        for row in rows:
            host = Host(row['name'], row['numberOfInterfaces'], row['id'])
            self.hosts_hash_map[host.get_id()] = host

    def insert_row_in_db(self, row):
        rows = []
        row['id'] = self.hash_function(row[self.get_attribute_for_matching()])
        host = Host(row['name'], row['numberOfInterfaces'], row['id'])
        self.hosts_hash_map[host.get_id()] = host
        for key in self.hosts_hash_map:
            row = self.hosts_hash_map[key]
            rows.append(row.get_json())
        self.db.update_db(self.file_name, rows)

    def insert_rows_in_db(self, rows):
        rows_to_insert_in_db = []
        for row in rows:
            row['id'] = self.hash_function(row[self.get_attribute_for_matching()])
            host = Host(row['name'], row['numberOfInterfaces'], row['id'])
            self.hosts_hash_map[host.get_id()] = host
        for key in self.hosts_hash_map:
            value = self.hosts_hash_map[key]
            rows_to_insert_in_db.append(value.get_json())
        self.db.update_db(self.file_name, rows_to_insert_in_db)


    def delete_row_db(self, id):
        del self.hosts_hash_map[id]
        rows = self.hosts_hash_map
        with open(self.file_name, 'w') as json_file:
            json_list = []
            for key_row in rows:
                json_data = rows[key_row].get_json()
                json_list.append(json_data)
            json.dump(json_list, json_file, indent=4)

    def delete_all(self):
        self.hosts_hash_map.clear()
        self.db.clear_db(self.file_name)

    def get_attribute_for_matching(self):
        return 'name'

    def hash_function(self, name):
        return hash(name) % 10000

