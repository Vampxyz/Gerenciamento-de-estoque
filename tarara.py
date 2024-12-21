import uuid
import mysql.connector
from datetime import datetime

# Gerenciamento de estoque 
stock = [
    {
    'Name': 'Carrinho hotweels 2009 - Mustang preto',
    'Description': 'carrinho mustang de brinquedo',
    'Stock': 16187113,
    'Price': 14.99,
    'ID': '0a6becb7263245e3b4cc9533f65ff752'
    },

    {
    'Name': 'Buzz Lightyear - Toy story',
    'Description': 'boneco de brinquedo do toy story',
    'Stock': 1481027340,
    'Price': 250.00,
    'ID': '0a6becb72da67sjahd134dag987svd91'
    }
]

def new_product():
    product = {
        "Name": str(input(f"\033[1mType the product name: \033[m")),
        "Description": str(input(f"\033[1mType a description for the product: \033[m")),
        "Stock": int(input(f"\033[1mType the available quantity of the Product: \033[m")),
        "Price": float(input(f"\033[1mType the price of the Product: \033[m")),
        "ID": uuid.uuid4().hex
    }

    stock.append(product)
    print(product)

def list_product():
    for product in range(len(stock)):
        print('\n')
        print('-------------------------------------------------------------------')
        print('\n')

        for key, value in stock[product].items():
            print(f"{key}: {value}")


# def update_product():

def remove_product():
    counter = 1
    for product in range(len(stock)):
        print('\n')
        print(f'--------------------------------- Produto {counter} ----------------------------------')
        print('\n')

        for key, value in stock[product].items():
            print(f"{key}: {value}")

        # print(f'-------------------------------------------------------------------')
        counter += 1

class Product:
    def __init__(self, id, name, description, stock, price):
        self.id = id
        self.name = name
        self.description = description
        self.stock = stock
        self.price = price        

class Sale:
    def __init__(self, product_id, quantity_sold, date_sale):
        self.product_id = product_id
        self.quantity_sold = quantity_sold
        self.date_sale = datetime.now

# new_product()
# list_product()
remove_product()

# SQL

class SalesSystem:
    def __init__(self):
        self.db = Database()

    def add_product(self, product):
        if not product.name or product.stock < 0 or product.price <= 0:
            print("Invalid datas, try again!")
            return None
        
        command = '''
            INSERT INTO products(name, description, stock, price)
            VALUES (%s, %s, %s, %s)
        '''
        datas = (product.name, product.description, product.stock, product.price)

        self.db.cursor.execute(command, datas)
        self.db.connection.commit()
        new_id = self.db.cursor.lastrowid
        print("Product added successfully")
        return new_id

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host = "localhost",
            port = 3306,
            user = "root",
            password = "Aluno123",
            database = "ge"
        )
        self.cursor = self.connection.cursor()
        print("\nConnection with DB established!")
        self.create_tables()

    def create_tables(self):
        command_create_product = '''
            CREATE TABLE IF NOT EXISTS products (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description TEXT,
                stock INT NOT NULL,
                price DECIMAL(10, 2) NOT NULL
            )
        '''
        self.cursor.execute(command_create_product)

        command_create_sales = '''
            CREATE TABLE IF NOT EXISTS sales (
                id INT AUTO_INCREMENT PRIMARY KEY,
                product_id INT,
                sale_quantity INT NOT NULL,
                data_venda DATETIME NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products(id)
            )
        '''
        self.cursor.execute(command_create_sales)
        self.connection.commit()
        print("Tables created succesfully")

db = Database()

