import json
from Models.CommonDBMethods import DB

class Link():

    class EndPoint():

        def __init__(self, name, interface, ip_address, mask):
            self.__name = name
            self.__interface = interface
            self.__ip_address = ip_address
            self.__mask = mask

        def get_name(self):
            return self.__name

        def get_interface(self):
            return self.__interface

        def get_ip_address(self):
            return self.__ip_address

        def get_mask(self):
            return self.__mask

        def get_json(self):
            json = {}
            json['name'] = self.__name
            json['interface'] = self.__interface
            json['ip_address'] = self.__ip_address
            json['mask'] = self.__mask
            return json

    def __init__(self, src, dst, bandwidth, id):
        self.__src = src
        self.__dst = dst
        self.__bandwidth = bandwidth
        self.__id = id

    def get_src(self):
        return self.__src

    def get_dst(self):
        return self.__dst

    def get_bandwidth(self):
        return self.__bandwidth

    def get_id(self):
        return self.__id

    def get_link(self):
        list = []
        list.append(self.get_src())
        list.append(self.get_dst())
        return list

    def get_link_json(self):
        obj = {}
        obj['src'] = self.get_src().get_json()
        obj['dst'] = self.get_dst().get_json()
        obj['bandwidth'] = self.get_bandwidth()
        obj['id'] = self.get_id()
        return obj

class LinkModel():

    def __init__(self):
        self.file_name = "/home/pedro/PycharmProjects/flask-intro/venv/code/Database/links.json"
        self.links_hash_map = {}
        self.db = DB()
        self.set_links_hash_map()

    def get_id(self, src_name, dst_name):
        conc = src_name + dst_name
        return hash(conc) % 10000

    def get_row(self, row):
        src = row['src']
        dst = row['dst']
        identifier = self.get_id(src, dst)
        if identifier in self.links_hash_map:
            link = self.links_hash_map[identifier]
            return link.get_link_json()

    def get_rows(self):
        rows = []
        for key in self.links_hash_map:
            #Return to the Client the way I want
            row = self.links_hash_map[key]
            rows.append(row.get_link_json())
        return rows

    def set_links_hash_map(self):
        rows = self.db.query_db(self.file_name)
        for row in rows:
            value_src = row['src']
            value_dst = row['dst']
            src_node = Link.EndPoint(value_src['name'], value_src['interface'], value_src['ip_address'], value_src['mask'])
            dst_node = Link.EndPoint(value_dst['name'], value_dst['interface'], value_dst['ip_address'], value_dst['mask'])
            link = Link(src_node, dst_node, row['bandwidth'], row['id'])
            self.links_hash_map[link.get_id()] = link


    def insert_row_in_db(self, link):
        rows = []
        value_src = link['src']
        value_dst = link['dst']
        src_node = Link.EndPoint(value_src['name'], value_src['interface'], value_src['ip_address'], value_src['mask'])
        dst_node = Link.EndPoint(value_dst['name'], value_dst['interface'], value_dst['ip_address'], value_dst['mask'])
        link_obj = Link(src_node, dst_node, link['bandwidth'], self.get_id(src_node.get_name(), dst_node.get_name()))
        self.links_hash_map[link_obj.get_id()] = link_obj
        for key in self.links_hash_map:
            value = self.links_hash_map[key]
            rows.append(value.get_link_json())
        self.db.update_db(self.file_name, rows)

    def insert_several_rows_in_db(self, rows):
        rows_to_insert_in_db = []
        for link in rows:
            value_src = link['src']
            value_dst = link['dst']
            src_node = Link.EndPoint(value_src['name'], value_src['interface'], value_src['ip_address'], value_src['mask'])
            dst_node = Link.EndPoint(value_dst['name'], value_dst['interface'], value_dst['ip_address'], value_dst['mask'])
            link_obj = Link(src_node, dst_node, link['bandwidth'], self.get_id(src_node.get_name(), dst_node.get_name()))
            self.links_hash_map[link_obj.get_id()] = link_obj
        for key in self.links_hash_map:
            value = self.links_hash_map[key]
            rows_to_insert_in_db.append(value.get_link_json())
        self.db.update_db(self.file_name, rows_to_insert_in_db)

    def delete_row(self, row):
        src = row['src']
        dst = row['dst']
        identifier = self.get_id(src, dst)
        if identifier in self.links_hash_map:
            del self.links_hash_map[identifier]
            rows = self.links_hash_map
            with open(self.file_name, 'w') as json_file:
                json_list = []
                for key_row in rows:
                    json_data = rows[key_row].get_link_json()
                    json_list.append(json_data)
                json.dump(json_list, json_file, indent=4)
            return "OK!"
        else:
            return "Invalid Name"

    def delete_all(self):
        self.links_hash_map.clear()
        self.db.clear_db(self.file_name)
