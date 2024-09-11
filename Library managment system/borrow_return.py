#2. Implement a module for book borrowing and returning. include function to borrow a book, return a book, and check a availability a book.
#3. Use the math module tocalculate fines for the late book returns based on a predefined formula.

from function import Library
import pandas as pd
import math
import time as t


borrow_data = []
data = pd.read_csv("Library managment system\\books.csv")
def borrow():
    global b_name
    global b_time
    b_name = input("Enter the name of the book you want to borrow. ")
    if b_name in data['name'].values:
        b_name_b = input("Enter  your name .. ")
        b_time = int(input("Enter the number of days you want to borrow.. "))
        borrow_data.append(b_name_b)
        borrow_data.append(b_time)
        print(f"You borrowed the book {b_name} for {b_time} at {t.time()}.Make sure that you return the book at time")
    else:
        print(f"{b_name} is not present in the Library")
    
def return_book():
    b_name = input("Enter the name of the book you want to return .. ")
    b_time = int(input("Enter the time at which you borroed the book"))
    if b_name in borrow_data:
        borrow_data.remove(b_name)
        borrow_data.append(b_time)
        print(f"You have returned the book {b_name}")
    else:
        print(f"This book is not in the register")
    
def calculate_fine():
    if b_time  <= 5:
        print("Hmm .. ")
        print(f"You have exceeded the time.. ")
        fine = b_time * 1
    else:
        fine = (5 * 1) + ((b_time -5 ) * 2)
    print(f"Your fine is {fine}$")

# List of books in the inventory with their overdue status
inventory = [
    {'title': 'Introduction to ML', 'days_overdue': 0},
    {'title': 'Deep Learning Basics', 'days_overdue': 3},
    {'title': 'Data Science with Python', 'days_overdue': 0},
    {'title': 'Artificial Intelligence', 'days_overdue': 5},
    {'title': 'Python for Data Analysis', 'days_overdue': 0}
]
def overdue():
    # Use a lambda function with filter to get overdue books
    overdue_books = list(filter(lambda book: book['days_overdue'] > 0, inventory))

    # Print the overdue books
    print("Overdue Books:")
    for book in overdue_books:
        return (book['title'], "- Overdue by", book['days_overdue'], "days")
   
         
         
def report():
    # Generate a report using list comprehensions
    borrowed_books_report = [f"{book['title']} (Overdue by {book['days_overdue']} days)"
           for book in inventory if book['days_overdue'] > 0]

    print("Borrowed Books Report:")
    for report in borrowed_books_report:
        print(report)
        
        
        
    
    
user = input("What do you want to do borrow, return , calculate fine, report")
if user == "borrow":
    borrow()
elif user == "return":
    return_book()
elif user == "calculate_fine":
    calculate_fine()
elif user == "report":
    report()            

if __name__ == "__main__":
    Library()           

    