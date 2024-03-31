class Employee:
    def __init__(self,surname,position,salary) -> None:
        self.surname = surname
        self.position = position
        self.salary = salary

class Enterprice_employee(Employee):
    def __init__(self, surname, position, salary,rating) -> None:
        super().__init__(surname, position, salary)
        self.rating = rating

    def __str__(self) -> str:
        return f"""Surname : {self.surname}
Position : {self.position}
Salary : {self.salary}
Rating : {self.rating}
"""
    
w1 = Enterprice_employee("Juraev","data science",3400,100)
w2 = Enterprice_employee("Haydarov","backend",350,7500)
w3 = Enterprice_employee("Hasanov","fronted",2300,60)
w4 = Enterprice_employee("Hamidullayev","junior",2300,80)
w5 = Enterprice_employee("Yusupov","middle",2500,86)

workers = [w1,w2,w3,w4,w5]

for worker in workers:
    if 60 <= worker.rating < 75:
        worker.salary *= 1.2
    elif 75 <= worker.rating < 90:
        worker.salary *= 1.4
    elif 90 <= worker.rating <= 100:
        worker.salary *= 1.6

for worker in workers:
    print(worker)

 