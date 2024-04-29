#atvaizduoti visus customerius
# import mysql.connector
#
# hostname = "localhost"
# username = "root"
# password = "865245929"
# database = "sakila"
#
# connection = None
# cursor = None
#
# try:
#     connection = mysql.connector.connect(host=hostname, port=3317, user=username, password=password, database=database)
#     print("Connection successful!")
#
#     cursor = connection.cursor()
#     query = "SELECT * FROM customer" # Replace with your desired query
#     cursor.execute(query)
#     results = cursor.fetchall()
#
#     for row in results:
#         print(f"ID: {row[0]}, Name: {row[2]}, Surname: {row[3]}") # Access column data by index
#
# except mysql.connector.Error as err:
#     print(f"Connection error: {err}")
#
# finally:
#     if cursor:
#         cursor.close()
#     if connection:
#         connection.close()
#     print("Connection closed.")

########################################
# atvaizduoti visus customerius ir stulpelį

# SELECT c.customer_id, count(*), sum(amount) FROM sakila.customer c
# JOIN payment p
# ON p.customer_id = c.customer_id
# GROUP BY c.customer_id

# import mysql.connector
#
# hostname = "localhost"
# username = "root"
# password = "865245929"
# database = "sakila"
#
# connection = None
# cursor = None
#
# try:
#     connection = mysql.connector.connect(host=hostname, port=3317, user=username, password=password, database=database)
#     print("Connection successful!")
#
#     cursor = connection.cursor()
#     query = "SELECT c.customer_id, count(*), sum(amount) FROM sakila.customer c JOIN payment p ON p.customer_id = c.customer_id GROUP BY c.customer_id" # Replace with your desired query
#     cursor.execute(query)
#     results = cursor.fetchall()
#
#     for row in results:
#         print(f"ID: {row[0]}, Count: {row[1]}, SumAmount: {row[2]}") # Access column data by index
#
# except mysql.connector.Error as err:
#     print(f"Connection error: {err}")
#
# finally:
#     if cursor:
#         cursor.close()
#     if connection:
#         connection.close()
#     print("Connection closed.")

##########################################
# atvaizduoti visus filmus ir kiek aktorių juose vaidino

import SQLCRUD as sql
#
# result = sql.readSQL("SELECT f.title, count(fa.actor_id) FROM sakila.film f JOIN sakila.film_actor fa ON f.film_id = fa.film_id GROUP BY f.title")
# for row in result:
#     print(f"Filmo Pavadinimas: {row[0]}, Vaidinusiu aktoriu kiekis: {row[1]}")

##########################################
# atvaizduoti aktorius ir keliuose filmuose jie yra filmavesi

# result = sql.readSQL("SELECT a.first_name, a.last_name, count(fa.film_id) FROM sakila.actor a JOIN sakila.film_actor fa ON a.actor_id = fa.actor_id GROUP BY a.first_name, a.last_name")
# for row in result:
#     print(f"Vardas: {row[0]}, Pavarde: {row[1]}, Filmavosi tiek kartu: {row[2]}")

##########################################
#kuris nuomos punktas: turi daugiau customerių

result = sql.readSQL("SELECT s.store_id, count(c.customer_id) FROM sakila.store s JOIN sakila.customer c ON s.store_id = c.store_id GROUP BY s.store_id")
for row in result:
    print(f"Store ID: {row[0]}, Customers: {row[1]}")

##########################################
# kuris nuomos punktas: išnuomavo daugiau(ir kiek kiekvienas) filmų



