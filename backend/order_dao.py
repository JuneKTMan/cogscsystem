from datetime import datetime


def insert_order(connection, order):
    cursor = connection.cursor()
    order_query = ("INSERT INTO cogscafetria.order(customer_name, total_cost, date_time) "
                   "VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['total_cost'], datetime.now())

    cursor.execute(order_query,order_data)
    order_id = cursor.lastrowid
    # in order_details table order id not a PK so it can be duplicate
    order_details_query = ("INSERT INTO cogscafetria.order_details (order_id, product_id, quantity, total_price)"
                           "VALUES (%s, %s, %s, %s)")
    order_details_data = []
    for order_details_record in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_details_record['product_id']),
            float(order_details_record['quantity']),
            float(order_details_record['total_price'])
        ])
    cursor.executemany(order_details_query, order_details_data)

    #important!! implement the update into the database
    connection.commit()

    return order_id

def get_all_order(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM cogscafetria.order")
    cursor.execute(query)

    response = []
    for (order_id, customer_name, total_cost, date_time) in cursor:
        response.append({
            'order_id' : order_id,
            'customer_name' : customer_name,
            'total_cost' : total_cost,
            'date_time': date_time

        })

    return response


if __name__ == '__main__':
    from sql_connection import get_sql_connection
    connection = get_sql_connection()

    print(get_all_order(connection))

    # print(insert_order(connection, {
    #     'customer_name': 'hello',
    #     'total_cost': '50',
    #     'order_details': [
    #         {
    #             'product_id': 20,
    #             'quantity': 2,
    #             'total_price':10
    #          },
    #         {
    #             'product_id': 10,
    #             'quantity': 2,
    #             'total_price': 20
    #         }
    #     ]
    #
    #     }))
