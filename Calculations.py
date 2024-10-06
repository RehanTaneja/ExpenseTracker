import datetime

class Calculator:
    def __init__(self):
        pass

    def total(self,rdr:list):
        sum=0
        for rec in rdr:
            sum+=int(rec[1])
        return sum
    
    def total_month(self,rdr:list,month):
        sum=0
        for rec in rdr:
            if datetime.datetime.strptime(rec[2],"%Y-%m-%d").date().month==month:
                sum+=int(rec[1])
        if sum==0:
            return "No Expense"
        return sum
    
    def total_year(self,rdr:list,year):
        sum=0
        for rec in rdr:
            if datetime.datetime.strptime(rec[2],"%Y-%m-%d").date().year==year:
                sum+=int(rec[1])
        if sum==0:
            return "No Expense"
        return sum  
