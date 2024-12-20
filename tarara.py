import uuid

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
    print('\n')
    print('-------------------------------------------------------------------')
    print('\n')
    for product in range(len(stock)):

        for key, value in stock[product].items():
            print(f"{key}: {value}")
        print("\n")
        print('-------------------------------------------------------------------')
        print("\n")


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
    def __init__(self, sale_id, product_id, quantity_sold, date_sale):
        self.sale_id = sale_id
        self.product_id = product_id
        self.quantity_sold = quantity_sold
        self.date_sale = date_sale

# new_product()
# list_product()
remove_product()