# 2 დავალება

# class Calculator:
#
#     def jami(a, b):
#         return a + b
#
#     def sxvaoba(a, b):
#         return a - b
#
#     def gayofa(a, b):
#         return a / b
#
#     def gamravleba(a, b):
#         return a * b
#
# a = Calculator.jami(10, 5)
# print(a)
#
# b = Calculator.sxvaoba(10, 5)
# print(b)
#
# c = Calculator.gayofa(10, 5)
# print(c)
#
# d = Calculator.gamravleba(10, 5)
# print(d)



# 3 დავალება

# class Rectangle:
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#
#     def area(self):
#         return self.width * self.length
#
#     def perimeter(self):
#         return 2*(self.width + self.length)
#
#     def print_info(self):
#         return print(f"სიგრძე - {self.length}, სიგანე - {self.width}, ფართობი - {self.area()}, პერიმეტრი - {self.perimeter()}")
#
# a = Rectangle(5, 4)
# a.print_info()



# 4 დავალება

class Employee:

    def __init__(self, name, surname, age, salary):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    list_names = []
    list_surnames = []
    list_ages = []
    list_salaries = []
    a = open("dataset1.csv", "r")
    for i in range(100):
        temp = ""
        b = a.readline()
        b = b.split(",")
        list_names.append(b[0])
        list_surnames.append(b[1])
        list_ages.append(b[2])
        count = 1
        for j in b[3]:
            if count > 4:
                list_salaries.append(temp)
                break
            temp = temp + j
            count = count + 1
    a.close()

    def print_info(self):
        return print(f"სახელი: {self.name}, გვარი: {self.surname}, ასაკი: {self.age}, ხელფასი: {self.salary}")

    index = 0
    for i in list_salaries:
        if i == min(list_salaries):
            break
        else:
            index = index + 1
    print(f"ყველაზე დაბალი ხელფასის მქონე პირი: სახელი - {list_names[index]}, გვარი - {list_surnames[index]}, ასაკი {list_ages[index]}, ხელფასი - {list_salaries[index]} ")


    index1 = 0
    for i in list_ages:
        if i == max(list_ages):
            break
        else:
            index1 = index1 + 1
    print(f"ყველაზე ასაკიანი პირი: სახელი - {list_names[index1]}, გვარი - {list_surnames[index1]}, ასაკი - {list_ages[index1]}, ხელფასი - {list_salaries[index1]}")

test = Employee("Saxeli", "Gvari", "20", "5000")
test.print_info()
