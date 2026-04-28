import pickle
import os

storage = {}

if os.path.exists("data.pkl"):
    with open("data.pkl", "rb") as f:
        storage = pickle.load(f)

def add_expense():
     
        n = int(input("How many entries? "))

        try:
            for _ in range(n):
                key = input("Enter Category: ")
                value = int(input("Enter Amount: "))
                storage[key] = value  
        except Exception:
             print("Enter Valid things so that we can calculate!")

def view_expense():
     
     for key,value in storage.items():
          print(f"{key} : {value}tk")

def total_spent():
     
     total = sum(storage.values())
     print(f"Total spent : {total}tk")




while True:

    print("===Welcome to Expense Tracker!===")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Show total spent")
    print("4. Delete a expense")
    print("5. Exit program")

    choice = int(input("Enter your choice(1/2/3/4/5) : "))

    if choice==1:
         
        add_expense()


    elif choice==2:

         view_expense()
            
    elif choice==3:

         total_spent()

    elif choice==4:
         again = input("Which category do u want to delete?")
         del storage[again]
            
    elif choice==5:

        break

    else:
         print("Enter valid choice!")


with open("data.pkl", "wb") as f: 
    pickle.dump(storage, f)
