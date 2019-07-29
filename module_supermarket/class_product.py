from module_supermarket.class_text_constants import TextConstants
from datetime import datetime, date, timedelta

class Product():
    def __init__(self, code, description, stock, unit_price, expiration_date:date, product_type, discount, sold_products=0):
        self._code = code
        self._description = description
        self._stock = stock
        self._unit_price = unit_price
        self._expiration_date = expiration_date
        self._product_type = product_type
        self._discount = discount
        self._sold_products = sold_products

    def code(self) -> int:
        return self._code
    
    def description(self) -> str:
        return self._description
    
    def stock(self) -> int:
        return self._stock
    
    def unit_price(self) -> int:
        return self._unit_price
    
    def expiration_date(self)-> date:
        return self._expiration_date
    
    def product_type(self) -> str:
        return self._product_type
    
    def discount(self) -> str:
        return self._discount

    def sold_products(self) -> int:
        return self._sold_products
    
    def set_code(self, code:int):
        self._code =code
    
    def set_description(self, description:str):
        self._description = description
    
    def set_stock(self, stock:int):
        self._stock = stock
    
    def set_unit_price(self, unit_price:int):
        self._unit_price = unit_price

    def set_expiration_date(self, expiration_date:date):
        self._expiration_date = expiration_date
    
    def set_product_type(self, product_type:str):
        self._product_type = product_type
    
    def set_discount(self, discount:str):
        self._discount = discount

    def set_sold_products(self, sold_products:int):
        self._sold_products = sold_products

    def update_stock_limitRequired(self, required:int):
        if self.stock() < required:
            self.set_stock(10)
    
    def update_stock(self,amount:int):
        if self.stock() >= amount:
            self.set_stock(self.stock() - amount)
            self.set_sold_products(self.sold_products() + amount)
            return True
        return False
    
    def total_by_product(self, amount:int) -> int:
        if self.discount() == TextConstants.discount_yes:
            return (self.unit_price() * amount) * 0.9
        return self.unit_price() * amount

    def error_stock_amount(self) -> str:
        return  TextConstants.menu_productError_amount() + str(self.stock())

    def update_unit_price(self, porcent:int):
        porcent_price = (porcent * self.unit_price()) / 100 
        self.set_unit_price(self.unit_price() + porcent_price)
    
        

        

    
