
def get_producttype(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM product_type")
    cursor.execute(query)

    response = []
    for (product_type_id, product_type_name) in cursor:
        response.append({
            'product_type_id': product_type_id,
            'product_type_name': product_type_name
        })
    return response

if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    # print(get_all_product(connection))
    print(get_producttype(connection))