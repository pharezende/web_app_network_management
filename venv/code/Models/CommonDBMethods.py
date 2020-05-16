import json

class DB:

    def query_db(self, file_name):
        with open(file_name) as json_file:
            try:
                rows = json.load(json_file)
            except ValueError:
                rows = []
            return rows

    def update_db(self, file_name, rows):
        with open(file_name, 'w') as json_file:
            json.dump(rows, json_file, indent=4)


    def clear_db(self, file_name):
        with open(file_name, 'w') as json_file:
            json_list = []
            json.dump(json_list, json_file, indent=4)