class Employee:

    def __init__(self, name, ID, dept, job, salary):
        self.__name = name
        self.__ID = ID
        self.__dept = dept
        self.__job = job 
        self.__salary = salary

    def getname(self):
        return self.__name

    def getID(self):
        return self.__ID

    def getdept(self):
        return self.__dept

    def getjob(self):
        return self.__job

    def getsalary(self):
        return self.__salary

    
