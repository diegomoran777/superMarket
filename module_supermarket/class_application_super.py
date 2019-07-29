from module_supermarket.class_super import SuperMarket
from module_supermarket.class_text_constants import TextConstants
from module_supermarket.class_product import Product
from datetime import datetime, date, timedelta

class ApplicationSuper():

    def __init__(self):
        self._super = SuperMarket()
        self._required = 0

    def super(self):
        return self._super
    
    def get_required(self):
        return self._required
    
    def set_requiered(self, required):
        self._required = required

    def input_check_number(self, text, error):
        keep_asking = True
        while keep_asking:
            try:
                inp = int(input(text))
                keep_asking = False
            except:
                print(error)
        return inp


    def module_required_amount(self):
        if len(self.super().product_list()) == 0:
            print(TextConstants.text_list_product_empty)
        else:
            required_stock = self.input_check_number(TextConstants.text_amount_required, TextConstants.text_input_error)
            self.set_requiered(required_stock)
            self.super().replenish_stock(required_stock)
        
    def module_load(self):
        keep_asking = True
        while keep_asking:
            inp = input(TextConstants.text_load)
            if inp == "1":
                self.super().load_list_file()
                keep_asking = False
                if inp == "2":
                    self.super().load_list_bd()
                    keep_asking = False
                else:
                    print(TextConstants.text_input_error)

    def module_save(self):
        keep_asking = True
        while keep_asking:
            try:
                inp = input(TextConstants.text_save)
                if inp == "1":
                    self.super().save_file()
                    keep_asking = False
                    if inp == "2":
                        self.super().save_bd()
                        keep_asking = False
                        if inp == "3":
                            self.super().save_file()
                            self.super().save_bd()
                            keep_asking = False
                        else:
                            print(TextConstants.text_input_error)
            except ValueError:
                print(TextConstants.text_input_error)

    def module_update_price_product(self):
        if len(self.super().product_list()) == 0:
            print(TextConstants.text_list_product_empty)
        else:         
            back = "s"
            while back == "s":
                keep_asking = True
                while keep_asking:
                    code = input(TextConstants.text_input_code)
                    porcent = self.input_check_number(TextConstants.text_input_porcent, TextConstants.text_input_error)
                    if not self.super().update_priceProduct_by_code(porcent, code):
                        print(TextConstants.text_product_not_exist)
                        keep_asking = False
                    else:
                        keep_asking = False
                        print("EL PRECIO FUE MODIFICADO")
                back = input(TextConstants.text_asking_update)

    def module_remove_product(self):
        if len(self.super().product_list()) == 0:
            print(TextConstants.text_list_product_empty)
        else:
            back = "s"
            while back == "s":
                keep_asking = True
                while keep_asking:
                    code = input(TextConstants.text_input_code)
                    if self.super().product_exist(code):
                        self.super().remove_by_code(code)
                        keep_asking = False
                    else:
                        print(TextConstants.text_product_not_exist)
                        keep_asking = False
                back = input(TextConstants.text_asking_remove)

    def module_delivery_information(self):
        information = {}
        name = input("INGRESAR NOMBRE:")
        information["nombre"]=name
        telephone_number = input("TELEFONO:")
        information["telefono"] = telephone_number
        street = input("INGRESAR CALLE:")
        information["calle"] = street
        adress_number = input("ALTURA:")
        information["altura"] = adress_number
        apartment_floor=input("PISO Y DEPTO:")
        information["piso_depto"] = apartment_floor
        print(information)

    def module_print_product_list(self):
        if len(self.super().product_list()) == 0:
            print(TextConstants.text_list_product_empty)
        else:
            self.super().print_list_products()

    def module_best_seller_product(self):
        if len(self.super().product_list()) == 0:
            print(TextConstants.text_list_product_empty)
        else:
            print(TextConstants.text_product_best_seller, self.super().best_selling_product())

    def module_buy(self):
        back = "s"
        while back == "s":
            add_again = "again"
            while add_again != "n":
                code = input(TextConstants.text_input_code)
                if self.super().product_exist(code):
                    product = self.super().bring_product_by_code(code)
                   # product.update_stock_limitRequired(self.get_required())
                    subtotal = self.enter_amount(product)
                    self.super().add_ticket(product.description(), product.unit_price(), subtotal)
                    total =+ subtotal
                else:
                    print(TextConstants.text_product_not_exist)
                add_again = input(TextConstants.text_add_product)
            if len(self.super().ticket()) == 0:
                print(TextConstants.text_empty_ticket)
            else:
                self.super().print_ticket(total)    
            back = input(TextConstants.text_asking_buy_again)

    def enter_amount(self, product:Product):
        keep_asking = True
        while keep_asking:
            try:
                amount = int(input(TextConstants.text_enter_amount, product.description()))
                if product.update_stock(amount):
                    #product.update_stock_limitRequired(self.get_required())
                    subtotal = product.total_by_product(amount)
                    keep_asking = False
                else:
                    print(product.error_stock_amount())
            except ValueError:
                print(TextConstants.text_input_error)
        return subtotal

    def month(self):
        keep_asking = True
        while keep_asking:
            try:
                m = int(input("Month: ")) 
                if m >= 1 and m <= 12:
                    keep_asking = False
                else:
                    print(TextConstants.text_input_error)
            except ValueError:
                print(TextConstants.text_input_error)
        return m

    def day(self, month:int):
        keep_asking = True
        while keep_asking:
            try:
                d = int(input("Day: ")) 
                if month == 2 and (d >= 1 and d <= 28):
                    keep_asking = False
                    if (month == 4 or month == 6 or month == 9 or month == 11) and (d >=1 and d <= 30):
                        keep_asking = False
                        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (d >= 1 and d <= 31):
                            keep_asking = False  
                        else:
                            print(TextConstants.text_input_error)
            except ValueError:
                print(TextConstants.text_input_error)
        return d

    def module_add_product(self):
        exit = "again"
        while exit == "s":
            code = input(TextConstants.text_input_code)
            if  not self.super().product_exist(code):
                description = input("INGRESAR NOMBRE DEL PRODUCTO: ")
                stock = self.input_check_number(TextConstants.text_input_stock, TextConstants.text_input_error)
                unit_price = int(input("INGRESAR PRECIO UNITARIO: "))
                print("INGRESAR FECHA CON FORMATO Y-m-d:")
                y = self.input_check_number("Year: ", TextConstants.text_input_error)
                m = self.month()
                d = self.day(m)
                expiration_date = date(y, m, d)
                product_type = input("INGRESAR TIPO DE PRODUCTO")
                discount = ""
                sold_products = 0
                add_product = input(TextConstants.text_input_add_product)
                if add_product == "s":
                    product = Product(code, description, stock, unit_price, expiration_date, product_type, discount, sold_products)
                    self.super().add_product(product)
            else:
                print(TextConstants.text_product_exist)
            exit = input(TextConstants.text_input_add_other_product)
            

    def input_check_option(self):
        keep_asking = True
        while keep_asking:
            try:
                option = int(input(TextConstants.main_menu))
                if option == 0:
                    print(TextConstants.text_input_error)
                else:
                    keep_asking = False
            except ValueError:
                print(TextConstants.text_input_error)
        return option

    def console_superMarket(self):
        exit = 0
        self.module_load()
        self.super().remove_expired_product()
        self.super().product_add_discount()
        while exit != 9:
            option = self.input_check_option()
            if option == 1:
                self.module_required_amount()
            if option == 2:
                self.module_buy()
            if option == 3:
                self.module_add_product()
            if option == 4:
                self.module_update_price_product()
            if option == 5:
                self.module_remove_product()
            if option == 6:
                self.module_delivery_information()
            if option == 7:
                self.module_best_seller_product()
            if option == 8:
                self.module_print_product_list()
            if option == 9:
                self.module_save()
            




            