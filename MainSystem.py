from Transaction import Transaction
from csvManager import csvManager
from Calculations import Calculator

class System:
    def __init__(self, file):
        self.manager=csvManager(file)
        self.calculator=Calculator()
    
    def add_expense(self,expense:Transaction):
        self.manager.write([expense.get_name(),expense.get_amount(),expense.get_date()])
        print("Expense Added!!")
    
    def total(self):
        rdr=self.manager.read()
        return self.calculator.total(rdr)
    
    def total_month(self,month):
        rdr=self.manager.read()
        return self.calculator.total_month(rdr,month)
    
    def total_year(self,year):
        rdr=self.manager.read()
        return self.calculator.total_year(rdr,year)
    
    def clear_expenses(self):
        self.manager.clear()
        
    def get_list_of_expenses(self):
        l1=[]
        rdr=self.manager.read()
        for rec in rdr:
            l1+=rec
        return l1
sys1=System("Expenses.csv")
print(sys1.get_list_of_expenses())