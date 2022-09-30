class Employee:

    def __init__(self, name, ID, department, job, salary):
        self.__name = name
        self.__ID = ID
        self.__department = department
        self.__job = job 
        self.__salary = salary

    def getname(self):
        return self.__name

    def getID(self):
        return self.__ID

    def getdepartment(self):
        return self.__department

    def getjob(self):
        return self.__job

    def getsalary(self):
        return self.__salary

    
