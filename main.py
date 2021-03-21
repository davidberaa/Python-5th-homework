# 1

# class Book:
#     def __init__(self, book_name, author, release_date, amount_pages):
#         self._book_name = book_name
#         self._author = author
#         self._release_date = release_date
#         self._amount_pages = amount_pages
#
#     def info(self):
#         return print(f"წიგნის სახელი - {self._book_name}, ავტორი - {self._author}, გამოშვების წელი - {self._release_date}, გვერდების რაოდენობა - {self._amount_pages}")
#
# book1 = Book("სახელი", "ავტორი", "გამოშვების წელი", "გვერდების რაოდენობა")
# book1.info()
#
# book2 = Book("სახელი2", "ავტორი2", "გამოშვების წელი2", "გვერდების რაოდენობა2")
# book2.info()



# 2

# class List(list):
#     def max(self):
#         result = self[0]
#         for i in self:
#             if i > result:
#                 result = i
#         return result
#
#     def min(self):
#         result = self[0]
#         for i in self:
#             if i < result:
#                 result = i
#         return result
#
# list1 = List([3, 1, 4, 5, 2])
# print(list1.max())
# print(list1.min())



# 3

# class Animal:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def info(self):
#         return print(f"სახელი - {self._name}, ასაკი - {self._age}")
#
#
# class Dog(Animal):
#     def __init__(self, name, age, breed, color):
#         super().__init__(age, name)
#         self._breed = breed
#         self._color = color
#
#     def info(self):
#         print(f"სახელი - {self._name}, ასაკი - {self._age}, ასაკი - {self._age}, ჯიში - {self._breed}, ფერი - {self._color}")
#
# dog1 = Dog("Bobby", "5", "Labrador", "Black")
# dog1.info()



# 4

class CallMixin:
    def call(self):
        return print(f"Calling to {self._phone}")

class Person(CallMixin):
    def __init__(self, fname, lname, phone):
        self._fname = fname
        self._lname = lname
        self._phone = phone

    def info(self):
        return print(f"fname - {self._fname}, lname - {self._lname}, phone - {self._phone}")

person1 = Person("name", "lastname", "+995 555 55 55 55")
person1.call()





