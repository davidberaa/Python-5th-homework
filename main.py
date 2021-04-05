import sqlite3
connection = sqlite3.connect('census.db')

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS density(province_or_territory TEXT, population INTEGER, land_area REAL)")

cursor.execute("INSERT INTO density VALUES('Newfoundland and Labrador', 512930, 370501.69 )")
cursor.execute("INSERT INTO density VALUES('Prince Edward Island', 135294, 5684.39)")
cursor.execute("INSERT INTO density VALUES('Nova Scotia', 908007 , 52917.43)")
cursor.execute("INSERT INTO density VALUES('New Brunswick', 729498 , 71355.67)")
cursor.execute("INSERT INTO density VALUES('Quebec', 7237479, 1357743.08)")
cursor.execute("INSERT INTO density VALUES('Ontario', 11410046, 907655.59)")
cursor.execute("INSERT INTO density VALUES('Manitoba', 1119583, 551937.87)")
cursor.execute("INSERT INTO density VALUES('Saskatchewan', 978933, 586561.35)")
cursor.execute("INSERT INTO density VALUES('Alberta ', 2974807, 639987.12)")
cursor.execute("INSERT INTO density VALUES('British Columbia', 3907738, 926492.48)")
cursor.execute("INSERT INTO density VALUES('Yukon Territory', 28674, 474706.97)")
cursor.execute("INSERT INTO density VALUES('Northwest Territories', 37360, 1141108.37)")
cursor.execute("INSERT INTO density VALUES('Nunavut ', 26745, 1925460.18)")


# task 4
def print_info():
    cursor.execute("SELECT * FROM density")
    rows = cursor.fetchall()

    for i in rows:
        print(i)

print_info()



# task 5
def print_population_info():
    cursor.execute("SELECT population FROM density")
    rows = cursor.fetchall()

    for i in rows:
        print(i)

print_population_info()



# task 6
def print_pop_less_than_million():
    cursor.execute("SELECT DISTINCT province_or_territory FROM density WHERE population < 1000000")
    print(cursor.fetchall())

print_pop_less_than_million()



# task 7
def print_pop_less_than_million_more_than_5():
    cursor.execute("SELECT DISTINCT province_or_territory FROM density WHERE population < 1000000 OR population > 5000000")
    print(cursor.fetchall())

print_pop_less_than_million_more_than_5()



# task 8
def print_pop1_5():
    cursor.execute("SELECT DISTINCT province_or_territory FROM density WHERE population > 1000000 AND population < 5000000")
    print(cursor.fetchall())

print_pop1_5()



# task 9
def print_area_more_than_200k():
    cursor.execute("SELECT DISTINCT population FROM density WHERE land_area > 200000")
    print(cursor.fetchall())

print_area_more_than_200k()



# task 10 ------------------


connection.commit()
