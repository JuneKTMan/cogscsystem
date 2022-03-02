import mysql.connector

from sql_connection import get_sql_connection
#print all product
def get_all_product(connection):

    cursor = connection.cursor()

    query = ("SELECT product.product_id, product.product_name, product.type_id, product.unit_id, product.price_per_unit, uom.uom_name, product_type.product_type_name "
             "FROM cogscafetria.product inner join cogscafetria.uom on product.unit_id=uom.uom_id inner join cogscafetria.product_type on product.type_id=product_type.product_type_id;")

    cursor.execute(query)

    response = []

    for (product_id,product_name,type_id,unit_id,price_per_unit,uom_name, product_type_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'product_name': product_name,
                'type_id': type_id,
                'unit_id': unit_id,
                'price_per_unit': price_per_unit,
                'uom_name': uom_name,
                'product_type_name': product_type_name
            }
        )

    return response
# insert new product into database table
def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO cogscafetria.product (product_name,type_id,unit_id,price_per_unit) "
             "VALUES (%s, %s, %s, %s)")
    data = (product['product_name'],product['type_id'],product['unit_id'],product['price_per_unit'])
    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM cogscafetria.product WHERE product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

# Implement the ADD, DELETE Function here
if __name__=='__main__':
    connection = get_sql_connection()
    print(delete_product(connection, 86))