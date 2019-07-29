import sqlite3

class CreateBd():
    
    conn = sqlite3.connect("supermarket.db")
#crear tabla
    conn.execute('''create table products
                   (code varchar(50),
                    description varchar(50),
                    stock  integer,
                    unit_price integer,
                    expiration_date date format YYYY-MM-DD ,
                    product_type varchar(1),
                    discount varchar(50)),
                    sold_products integer;''')
print("tabla creada exitosamente")
