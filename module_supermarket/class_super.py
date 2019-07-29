from module_supermarket.class_product import Product
from datetime import datetime, date, timedelta
from module_supermarket.class_text_constants import TextConstants
import json
from module_supermarket.class_load import Load
from module_supermarket.class_save import Save
import sqlite3

class SuperMarket():
    def __init__(self):
        self._product_list = []
        self._expired_list = []
        self._ticket = {}
    
    def ticket(self):
        return self._ticket

    def product_list(self):
        return self._product_list
    
    def expired_list(self):
        return self._expired_list

    def set_product_list(self,product_list):
        self._product_list = product_list

    def set_expired_list(self,expired_list):
        self._expired_list = expired_list

    def set_ticket(self,ticket):
        self._ticket = ticket

    def remove_product(self, product:Product):
        self._product_list.remove(product)

    def remove_by_code(self, code):
        for product in self.product_list():
            if product.code() == code:
                self.remove_product(product)

    def add_product(self, product:Product):
        self._product_list.append(product)
    
    def add_product_to_expired_list(self, product:Product):
        self._expired_list.append(product)

    def remove_expired_product(self):
        current_date = date.today()
        for product in self.product_list():
            if product.expiration_date() < current_date:
                self.add_product_to_expired_list(product)
                self.remove_product(product)
    
    def product_exist(self,code):
        for product in self.product_list():
            if product.code() == code:
                return True
        return False

    def replenish_stock(self,required_stock:int):
        for product in self.product_list():
            product.update_stock_limitRequired(self,required_stock)
    
    def update_priceProduct_by_code(self, porcent:int, input_code:str):
        if self.product_exist(input_code):
            for product in self.product_list():
                if product.code() == input_code:
                    product.update_unit_price(porcent)
        else:
            return False

    def product_add_discount(self):
        date_discount = date.today() + timedelta(days=7)
        for product in self.product_list():
            if product.expiration_date() == date_discount:
                product.set_discount(TextConstants.discount_yes)
            else:
                product.set_discount(TextConstants.discount_no)

    def print_list_products(self):
        for product in self.product_list():
            print("NOMBRE:",product.description(),"STOCK:",str(product.stock()),"PRECIO",str(product.unit_price()),"FECHA DE VENCIMIMENTO",product.expiration_date(),"TIPO DE PRODUCTO:",product.product_type(),"DESCUENTO:",product.discount(), "PRODUCTOS VENDIDOS:",str(product.sold_products()), sep="\t")
    
    def add_ticket(self, description:str, unit_price:int, subtotal:int):
        self.ticket()[description] = [unit_price, subtotal]
    
    def print_ticket(self,total:int):
        print("NOMBRE","PRECIO UNITARIO","SUBTOTAL",sep="\t")
        for products,values in self.ticket().items():
            print(products,values,sep="\t")
        print("TOTAL:",total)
        self.ticket().clear()
    
    def bring_product_by_code(self, code) -> Product:
        for product in self.product_list():
            if product.code() == code:
                return product
        return False

    def best_selling_product(self):
        best_seller = 0
        name_product = "NINGUNO"
        for product in self.product_list():
            if best_seller < product.sold_products() and product.sold_products() != 0:
                best_seller = product.sold_products()
                name_product = product.description()
        return name_product

    def pass_to_json(self):
        dic_product = {}
        for product in self.product_list():
            dic_product[product.description()] = [product.code(),product.description(),product.stock(),product.unit_price(),product.expiration_date(),product.product_type(),product.discount(),product.sold_products()]
        return json.dumps(dic_product)

    def load_list_file(self):
        try:
            list_product_to_py = []
            json_productList = Load().load_file()
            for product in json_productList:
                product_to_py = Product(json_productList[product][0], json_productList[product][1], json_productList[product][2], json_productList[product][3], json_productList[product][4], json_productList[product][5], json_productList[product][6], json_productList[product][7])
                list_product_to_py.append(product_to_py)
            self.set_product_list(list_product_to_py)
        except:
            print(TextConstants.empty_list_notice()) 
    
    def load_list_bd(self):
        try:
            list_product_to_py = []
            load_bd = Load().load_bd()
            for row in load_bd: 
                product = Product(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
                list_product_to_py.append(product)
            self.set_product_list(list_product_to_py)
        except:
            print(TextConstants.empty_list_notice())

    def save_bd(self):
        Save().save_bd(self.product_list())

    def save_file(self):
        Save().save_file(self.pass_to_json())

    def bla(self):
        p="s"
        while p=="s":
            x="bla"
            while x != "n":
                x =input("desea agregar? n o cualquier para seguir")
            p=input("desea realizar otra s o cualquiera para salir")
        print("saliste")



