import os
import sqlite3
from module_supermarket.class_product import Product
from module_supermarket.class_text_constants import TextConstants

class Save():

    def save_file(self,json_parsed):
        try:
            os.remove("lista_product.json")
            file = open("lista_product.json" , "w")
            file.write(json_parsed)
            file.close()
        except:
            print(TextConstants.error_save())

    def save_bd(self,product_list:[]):
        try:
            conn = sqlite3.connect("supermarket.db")
            conn.execute("DELETE FROM products")
            conn.commit()
            for product in product_list:
                conn.execute("insert into products (code, description, stock, unit_price, expiration_date, product_type, discount, sold_products) values ('" + product.code() + "', '"  + product.description() + "', '" + product.stock() + "', '" + product.unit_price() + "','" + product.expiration_date() + "','" + product.product_type() + "','" + product.discount() + "','" + product.sold_products() + "')")
                conn.commit()
            conn.close()
        except:
            print(TextConstants.error_save())    

