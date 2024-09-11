#Build a library management system . The system needs to handle book borrowing, returning and inventory management. Implement functions and modules to perform these task efficiently..

#Task:
#1. Create a module to managing book inventory. Include functions to add books, remove books and display the current inventory.
#2. Implement a module for book borrowing and returning. include function to borrow a book, return a book, and check a availability a book.
#3. Use the math module tocalculate fines for the late book returns based on a predefined formula.
#4.  Demonstrate the use of lambda function to filter out overdue books from the inventory.
#5. utilize the list comprehensions to generate repoorts on borrowed books.
import csv
import pandas as pd

df = pd.read_csv("Library managment system\\books.csv")

print(df)

class Library():
            
    
    def add(self):
        """
        It adds book in a library"""
        row = []
        
        row.append(name)
        row.append(year)
        row.append(author)
        
        with open('books.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row) 
           
        print(f"{row} is added to your library")
    
    def remove(self):
        """ 
        It removes the book from the lirary if it exists"""
        row_remove = []
       
        row_remove.append(name)
        row_remove.append(year)
        row_remove.append(author)
        with open('books.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
        rows = [row for row in rows if row != row_remove]   
        
        with open('books.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
    def display(self):
        """
        It displays the current inventory"""
        data = pd.read_csv("Library managment system\\books.csv")
        df = pd.DataFrame(data)
        print(df)
        print(df.describe)
    

choice = input("What do you want to do add or remove book or display: ")
if choice == "add":
    name = input("Enter the name of the book.. ")
    year = int(input("Enter the year of pubish.  "))
    author = input("Enter the name of the author. ")   
    library = Library(name, year, author)
    library.add()
elif choice == "remove":
    name = input("Enter the name of the book.. ")
    year = int(input("Enter the year of pubish.  "))
    author = input("Enter the name of the author. ")   
    library = Library(name, year, author)    
    library.remove()
elif choice == "display":
     
    library = Library()
    library.display()        
