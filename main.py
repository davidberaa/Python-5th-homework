import sqlite3

connection = sqlite3.connect("dataset2.db")

cursor = connection.cursor()

# cursor.execute("CREATE TABLE dataset2('OrderDate' TEXT, 'Region' TEXT, 'Client' TEXT, 'Item' TEXT, 'Units' INTEGER, 'UnitCost' REAL, 'Total' REAL)")


# a = open("dataset2.csv", "r")
#
# for i in range(43):
#     temp = ""
#     b = a.readline()
#     b = b.split(",")
#     cursor.execute(f"INSERT INTO dataset2 VALUES('{b[0]}', '{b[1]}', '{b[2]}', '{b[3]}', '{b[4]}', '{b[5]}', '{b[6]}')")
# a.close()



# task 1

# cursor.execute("SELECT SUM(Total) FROM dataset2 WHERE REGION = 'Central'")
# print(cursor.fetchall())
# cursor.execute("SELECT SUM(Total) FROM dataset2 WHERE REGION = 'East'")
# print(cursor.fetchall())
# cursor.execute("SELECT SUM(Total) FROM dataset2 WHERE REGION = 'West'")
# print(cursor.fetchall())



# task 2

# cursor.execute("SELECT Client FROM dataset2 WHERE Total = MAX(Total)")
# print(cursor.fetchall())



# task 3

# cursor.execute("SELECT Product FROM dataset2 WHERE Total = MAX(Total)")
# print(cursor.fetchall())



# task 4

# cursor.execute("SELECT AVG(UnitCost) FROM dataset2")
# print(cursor.fetchall())



# task 5

cursor.execute("SELECT SUM(Total) FROM dataset2")
print(cursor.fetchall())

connection.commit()

