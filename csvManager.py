import csv

class csvManager:
    def __init__(self,file:csv):
        self.file=file
    
    def write(self,rec:list):
        f1=open(self.file,'a')
        wrtr=csv.writer(f1)
        wrtr.writerow(rec)
        f1.close()
    
    def read(self):
        f1=open(self.file,'r')
        r=csv.reader(f1)
        rdr=[]
        for rec in r:
            rdr+=[rec]
        f1.close()
        return rdr
    
    def clear(self):
        f1=open(self.file,'w')
        f1.close()
    