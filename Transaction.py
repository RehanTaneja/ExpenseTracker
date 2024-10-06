import datetime

class Transaction:
    def __init__(self, name, amount, date=datetime.date.today()):
        self.name=name
        self.amount=amount
        self.date=date
    
    def __str__(self):
        return (self.name, ", ",self.amount,", ",self.date)
    
    def get_name(self):
        return self.name
    
    def get_amount(self):
        return self.amount
    
    def get_date(self):
        return self.date
    

