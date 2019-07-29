import json
import sqlite3
from module_supermarket.class_text_constants import TextConstants

class Load():

    def load_file(self):
        try:
            file = open("product_list.json","r")
            json_parsed = file.read()
            file.close()
            return json.loads(json_parsed)
        except:
            print(TextConstants.error_load())
    
    def load_bd(self):
        try:
            conn = sqlite3.connect("supermarket.db")
            load = conn.execute("select * from products")
            conn.close()
            return load
        except:
            print(TextConstants.error_load())
            
