import mysql.connector

config = {
    'user': 'Mariabejide',
    'password': 'Tomtom8989!',
    'host': 'cis3368db.cybkzz9d0l5t.us-east-1.rds.amazonaws.com',
    'database': 'CIS3368DB',
    'port': 3306  
}

db_connection = mysql.connector.connect(**config)


cursor = db_connection.cursor(dictionary=True)

sql = "SELECT * FROM sales"
cursor.execute(sql)

results = cursor.fetchall()

if not results:
    print("No data found.")
else:
    for row in results:
        print(row)

    print('')

    total_sales = 0

    user_query = input('Enter a seller name: ')
    print(f'Sales Report for {user_query}')

    for row in results:
        if row['seller'] == user_query:
            total_overall_sales = row['quantity'] * row['price']  
            print(f"Product: {row['product']}, Quantity: {row['quantity']}, Price: ${row['price']:.2f}, Total: ${total_overall_sales:.2f}")
            total_sales += total_overall_sales

    print(f"Total sales for {user_query}: ${total_sales:.2f}")

cursor.close()
db_connection.close()

