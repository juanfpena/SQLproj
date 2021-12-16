"""Generate random values to be used for the 'seed_tables.py' file"""
import random
import string
import datetime
from typing import Dict, List, Union
from id_selector import product_id_in_purchase

def random_expense_family_engine(num_families: int) -> List[Dict]:
    """Creates list of json objects to seed expense_family table for testing purposes."""

    my_families = []

    for i in range(num_families):
        random_family = ''.join(random.choices(string.ascii_letters, k=6))
        my_families.append(random_family)

    my_list = [{"service_name": family} for family in my_families]

    return my_list

def random_purchase_engine(num_purchases: int, product: List) -> List[Dict]:
    
    my_list = []
    product_num = len(product)

    def get_product_price(product: List) -> List:

        my_price_list = []

        for i in range(product_num):
            my_price = product[i]["price"]

            my_price_list.append(my_price)

        return my_price_list

    product_price = get_product_price(product = product)

    for i in range(num_purchases):
        product_id = random.randint(1, product_num)
        cost = random.randint(1,random.choice(product_price))
        quantity = random.randint(1,300)
        in_stock = random.randint(0,quantity)
        
        created_at = datetime.datetime(
            random.randint(2010, 2021),
            random.randint(1, 12),
            random.randint(1, 28),
            random.randint(1, 23),
            random.randint(1, 59),
            random.randint(1, 59)
        )

        random_row = {
            "product_id": product_id,
            "quantity": quantity,
            "cost": cost,
            "in_stock": in_stock,
            "created_at": created_at

        }
        my_list.append(random_row)
    return my_list

def random_expense_item_engine(num_expenses: int, families: List) -> List[Dict]:
    """Creates list of json objects to seed expense_item table for testing purposes."""

    my_list = []
    num_families = len(families)

    for i in range(num_expenses):
        item_name = ''.join(random.choices(string.ascii_letters, k=10))
        item_family = random.randint(1, num_families)
        item_cost = random.uniform(0.0, 20000.0)

        random_row = {
            "item_name": item_name,
            "family_id": item_family,
            "cost": item_cost
        }

        my_list.append(random_row)

    return my_list


def random_assigned_expense_item_engine(num_assigned_expenses: int, items: List) -> List[Dict]:
    """Creates list of json objects to seed assigned_expense_item table for testing purposes."""

    my_list = []
    num_items = len(items)
    for i in range(num_assigned_expenses):
        item_id = random.randint(1, num_items)

        created_at = datetime.datetime(
            random.randint(2010, 2021),
            random.randint(1, 12),
            random.randint(1, 28),
            random.randint(1, 23),
            random.randint(1, 59),
            random.randint(1, 59)
        )

        state = random.choice(['pagado', 'no pagado'])

        random_row = {
            "item_id": item_id,
            "state": state,
            "created_at": created_at
        }

        my_list.append(random_row)

    return my_list


def random_product_engine(num_products: int) -> List[Dict]:
    """Creates list of json objects to seed product table for testing purposes."""

    my_list = []

    for i in range(num_products):

        price = random.randint(0, 100000)
        
        random_row = {
            "price": price,
        }
        my_list.append(random_row)
    return my_list


def random_sale_engine(num_sales: int, product: List, customer: List) -> List[Dict]:
    """Creates list of json objects to seed sale table for testing purposes."""

    my_list = []
    num_product = len(product)
    num_customer = len(customer)

    for i in range(num_sales):
        product_id = random.randint(1, num_product)
        created_at = datetime.datetime(
            random.randint(2010, 2021),
            random.randint(1, 12),
            random.randint(1, 28),
            random.randint(1, 23),
            random.randint(1, 59),
            random.randint(1, 59)
        )
        quantity = random.randint(1, 500)
        customer_table_id = random.randint(1, num_customer)
        
        random_row = {
            "product_id": product_id,
            "created_at": created_at,
            "quantity": quantity,
            "customer_table_id": customer_table_id
        }

        my_list.append(random_row)
    return my_list

def random_customer_table_engine(num_customer: int) -> List[Dict]:

    my_list = []

    for i in range(num_customer):
        name = "".join(random.choices(string.ascii_letters, k=10))
        surname = "".join(random.choices(string.ascii_letters, k=10))
        phone_number = int(''.join(
                    random.choices(
                        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'], k=9)
                ))
        email = "".join(random.choices(string.ascii_letters, k=10))

        random_row = {
            "name": name,
            "surname": surname,
            "phone_number": phone_number,
            "email": email
        }

        my_list.append(random_row)

    return my_list

def random_sale_to_purchase_engine(sale: List[Dict]) -> List[Dict]:
    print(sale)
    my_list = []

    for i in range(1):
        sale_id = i
        quantity = sale[i]["quantity"]
        product_id = sale[i]["product_id"]
        print(quantity, product_id)# -> 474 1

        purchase_list = product_id_in_purchase(sale_quantity=quantity, product_id=product_id)
        
        print(purchase_list)# -> []

        for purchase_dict in purchase_list:

            random_row = {
                "sale_id": sale_id,
                "purchase_id": purchase_dict["purchase_id"],
                "quantity": purchase_dict["quantity"]
            }

            my_list.append(random_row)
    print(my_list) 
     