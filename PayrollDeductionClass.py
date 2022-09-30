class PayrollDeduction:
    def __init__(self, desc, date, amt, ID):
        self.__desc = desc
        self.__date = date
        self.__amt = amt
        self.__ID = ID

    def getdesc(self):
        return self.__desc

    def getdate(self):
        return self.__date

    def getamt(self):
        return self.__amt

    def getID(self):
        return self.__ID

        
