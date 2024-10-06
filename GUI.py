from MainSystem import System
from Transaction import Transaction
from tkinter import messagebox
import tkinter as tk

class GUI:
    def __init__(self):
        self.sys=System('Expenses.csv')
        self.root=tk.Tk()

        self.root.geometry("1100x300")
        self.root.title("Expense Tracker")
        self.label_name=tk.Label(self.root,text="Name:",font=('Arial',18),height=1)
        self.label_amount=tk.Label(self.root,text="Amount:",font=('Arial',18),height=1)
        self.label_date=tk.Label(self.root,text="Date(YYYY-MM-DD):",font=('Arial',18),height=1)
        self.textbox_name=tk.Text(self.root,font=('Arial',18),height=1)
        self.textbox_amount=tk.Text(self.root,font=('Arial',18),height=1)
        self.textbox_date=tk.Text(self.root,font=('Arial',18),height=1)
        self.button_add_expense=tk.Button(self.root,font=('Arial',18),command=self.add_expense,text="Add Expense",height=1)
        self.button_total=tk.Button(self.root,font=('Arial',18),command=self.total,text="Total",height=1)
        self.button_total_month=tk.Button(self.root,font=('Arial',18),command=self.total_month,text="Total-Month",height=1)
        self.button_total_year=tk.Button(self.root,font=('Arial',18),command=self.total_year,text="Total-Year",height=1)
        self.button_clear_expenses=tk.Button(self.root,font=('Arial',18),command=self.clear_expenses,text="Clear Expenses",height=1)
        self.button_get_list_of_expenses=tk.Button(self.root,font=('Arial',18),command=self.get_list_of_expenses,text="Get List Of Expenses",height=1)

        self.frame=tk.Frame(self.root)
        self.frame.columnconfigure(0,weight=1)
        self.frame.columnconfigure(1,weight=1)
        self.label_name.grid(row=0,column=0,sticky=tk.W+tk.E)
        self.textbox_name.grid(row=0,column=1,sticky=tk.W+tk.E)
        self.label_amount.grid(row=1,column=0,sticky=tk.W+tk.E)
        self.textbox_amount.grid(row=1,column=1,sticky=tk.W+tk.E)
        self.label_date.grid(row=2,column=0,sticky=tk.W+tk.E)
        self.textbox_date.grid(row=2,column=1,sticky=tk.W+tk.E)
        self.button_add_expense.grid(row=3,column=0,sticky=tk.W+tk.E)
        self.button_clear_expenses.grid(row=3,column=1,sticky=tk.W+tk.E)
        self.button_get_list_of_expenses.grid(row=4,column=0,sticky=tk.W+tk.E)
        self.button_total.grid(row=4,column=1,sticky=tk.W+tk.E)
        self.button_total_month.grid(row=5,column=0,sticky=tk.W+tk.E)
        self.button_total_year.grid(row=5,column=1,sticky=tk.W+tk.E)

        self.root.mainloop()

    def add_expense(self):
        name=self.textbox_name.get('1.0',tk.END).strip()
        amount=self.textbox_amount.get('1.0',tk.END).strip()
        date=self.textbox_date.get('1.0',tk.END).strip()
        t=Transaction(name,amount,date)
        self.sys.add_expense(t)
        messagebox.showinfo(title="Message",message="Expense Added!!")

    def clear_expenses(self):
        self.sys.clear_expenses()
        messagebox.showinfo(title="Messsage",message="Expenses Cleared!!")

    def total(self):
        total=self.sys.total()
        messagebox.showinfo(title="Message",message=total)

    def total_month(self):
        popup=tk.Toplevel(self.root)
        popup.geometry("300x300")
        popup.title("Monthly Total")
        label=tk.Label(popup,text="Month:",font=('Arial',18))
        label.pack(pady=10)
        tbox=tk.Text(popup,font=('Arial',18),height=1)
        tbox.pack(pady=5)
        def process_input():
            month=int(tbox.get('1.0',tk.END).strip())
            total_month=self.sys.total_month(month)
            messagebox.showinfo(title="Message",message=total_month)
        btn1=tk.Button(popup,text="Enter",command=process_input,font=('Arial',18))
        btn1.pack(pady=10)

    def total_year(self):
        popup=tk.Toplevel(self.root)
        popup.geometry("300x300")
        popup.title("Yearly Total")
        label=tk.Label(popup,text="Year:",font=('Arial',18))
        label.pack(pady=10)
        tbox=tk.Text(popup,font=('Arial',18),height=1)
        tbox.pack(pady=5)
        def process_input():
            year=int(tbox.get('1.0',tk.END).strip())
            total_year=self.sys.total_year(year)
            messagebox.showinfo(title="Message",message=total_year)
        btn1=tk.Button(popup,text="Enter",command=process_input,font=('Arial',18))
        btn1.pack(pady=10)

    def get_list_of_expenses(self):
        l1=self.sys.get_list_of_expenses()
        expense=[]
        for i in range(0,len(l1)-3,3):
            name=l1[i]
            amount=l1[i+1]
            date=l1[i+2]
            expense.append(f"{name}:{amount}:{date}")
        l2="\n".join(expense)
        messagebox.showinfo(title="List Of Expenses",message=l2)