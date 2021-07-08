
#------------------------
# Decorators
import time

def calc_time(func):
    """Calculate the time spent in the function"""
    def temp(*args, **kwargs):
        start_time = time.time()
        function=func(*args, **kwargs)
        end_time = time.time()
        print("Excuted in {} second".format(end_time-start_time))
        return function
    return temp

#------------------------

# dunder methods

class Student:
    def __init__(self, name) -> None:
        self.name = name
        

    def __str__(self) -> str:
        return self.name

class ClassRoom:

    def __init__(self) -> None:
        self.students = []

    def __add__(self, other):
        return self.students + other.students

# iterators

    def __iter__(self):
        for student in self.students:
            yield student

#------------------------



if __name__ == "__main__":

    @calc_time
    def ex(ls):
        # wasting time
        for i in ls:
            print(i)

    ex([1,2,3])

    stu1 = Student("Ahmad")
    stu2 = Student("Ayman")
    stu3 = Student("Mohammed")
    stu4 = Student("Ali")
    
    clsroom1 = ClassRoom()
    clsroom2 = ClassRoom()
    
    clsroom1.students.append(stu1)
    clsroom1.students.append(stu2)

    clsroom2.students.append(stu3)
    clsroom2.students.append(stu4)

    for stu in clsroom1:
        print(stu)

    clsroom3 = clsroom1+clsroom2
    assert [stu.name for stu in clsroom3] == ['Ahmad', 'Ayman', 'Mohammed', 'Ali']
