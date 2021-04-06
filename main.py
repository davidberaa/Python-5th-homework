# task 1
# class MyList:
#     def __init__(self, *args):
#         self._args = args
#
#         data = []
#         for i in self._args:
#             data.append(i)
#
#     def __add__(self, other):
#         newlist = self._args + other._args
#         return list(newlist)
#
#
#     def __mul__(self, other):
#         newlist = self._args * other
#         return list(newlist)
#
#     def __str__(self):
#         return str(self._args)
#
#
# l1 = MyList(1, 2, 3)
# l2 = MyList(4, 5)
#
# print(l1 + l2)
#
# print(l1 * 2)
#
# print(str(l1))



# task 2
"""არასრულყოფილია ეს დავალება, მაგრამ როგორც შემეძლო ისე დავწერე"""
class Testpaper:

    def __init__(self, subject, mark_scheme, pass_mark):
        self._subject = subject
        self._mark_scheme = mark_scheme
        self._pass_mark = pass_mark

    def get_subject(self):
        return self._subject

    def get_mark_scheme(self):
        return self._mark_scheme

    def get_pass_mark(self):
        return self._pass_mark

class Student():

    def take_test(self, subject, mark_scheme):


        def check_answers():
            correct = 0
            wrong = 0
            mark_scheme = Testpaper.get_mark_scheme()

            for i in mark_scheme:
                for j in self._mark_scheme:
                    if i == j:
                        correct = correct + 1
                    else:
                        wrong = wrong + 1
            answer_count = correct + wrong
            result = (correct * 100) / answer_count
            result = round(result)

            return result


        self._subject = subject
        self._mark_scheme = mark_scheme
        subject = Testpaper.get_subject()
        pass_mark = Testpaper.get_pass_mark()

        if self._subject == subject:
            if check_answers() >= pass_mark:
                print(f"{self._subject} : Passed! ({str(check_answers()) + '%'})")
            else:
                print(f"{self._subject} : Failed! {str(check_answers()) + '%'})")


Maths = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60")

student1 = Student
student1.take_test("Maths", ["1A", "2C", "3D", "4A", "5C"])
