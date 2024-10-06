# ExpenseTracker
An expense tracker that keeps record of expenses in a csv file and has a GUI made from tkinter. This project has been made using OOPS in python
## Features
* **Add Expense**: Input the name, amount, and date of an expense.
* **View Expenses**: Display a list of all recorded expenses.
* **Calculate Totals**: Get total expenses for a selected month or year.
* **Clear Expenses**: Remove all recorded expenses.
* **Data Storage**: Expenses are stored in a CSV file for easy access and management.
* **Monthly Total**: Calculates and displays the total expenditure of a month entered by the user
* **Yearly Total**: Calculates and displayes the total expenditure of a year entered by the user
## Requirements
* Python 3.12
* Tkinter
## Installation
1. **Clone the repository**:
```
git clone https://github.com/RehanTaneja/ExpenseTracker.git
```
2. **Run the Application**
```
python3 main.py
```
## Project Structure
ExpenseTracker/
* main.py          # Main application file
* MainSystem.py    # Class for handling overall functions
* Transaction.py   # Class for individual transactions
* Calculator.py    # Class for performing calculations like total, monthly total and yearly total
* GUI.py           # Class for making GUI using tkinter
* Expenses.csv     # CSV file for storing expenses
* csvManager.py    # Class for handling csv read, write functions
## Usage
1. Launch the application.
2. Enter the name, amount, and date of the expense in the respective fields. **DO NOT PRESS ENTER AFETR TYPING**
3. Click "Add Expense" to save the expense.
4. Use the buttons to view totals,clear expenses and list them.
## Acknowledgements
Thanks to the open-source community for libraries and resources that made this project possible.

