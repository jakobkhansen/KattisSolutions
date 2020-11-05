import sys
import operator

class Employee:
    def __init__(self, id, salary, height):
        self.id = id
        self.salary = salary
        self.height = height
        self.boss = None
        self.subordinates = 0

def whostheboss():
    firstLine = sys.stdin.readline()
    m = int(firstLine.split()[0])
    q = int(firstLine.split()[1])

    employees = []
    lookup = {}
    for _ in range(m):
        employee = [int(x) for x in sys.stdin.readline().split()]
        employee_obj = Employee(employee[0], employee[1], employee[2])
        employees.append(employee_obj)
        lookup[employee_obj.id] = employee_obj


    employees.sort(key=getSalary)
    # print(list(map(getId, employees)))
    # print(list(map(getSalary, employees)))

    for i,employee in enumerate(employees):
        for j in range(i+1, len(employees)):
            if (employees[j].height >= employee.height):
                employee.boss = employees[j]
                break

    for employee in employees:
        current = employee
        while current.boss != None:
            # print("boss of {} is {}".format(employee.id, employee.boss.id))
            # print("loop")
            current.boss.subordinates += 1
            current = current.boss

    retString = ""
    for _ in range(q):
        query_index = int(sys.stdin.readline().split()[0])
        employee = lookup[query_index]
        boss = employee.boss.id if employee.boss != None else 0
        retString += "{} {}\n".format(boss, employee.subordinates)
    print(retString.strip())


def findEmployeeIndex(employees, employee_id):
    for employee in employees:
        if employee.id == employee_id:
            return employee

def getId(employee):
    return employee.id

def getSalary(employee):
    return employee.salary


def main():
    whostheboss()
main()
