from storage import *
import time

def main():
    while True:
        print("-------------------------------------------------------------------------------------")
        print("Welcome to the Bank Management System")
        print("1. Add Customer")
        print("2. Display Customers")
        print("3. Perform Transaction")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            customer_name = input("Enter Customer Name: ")
            balance = float(input("Enter Balance: "))
            add_customer(customer_name, balance)
            
        elif choice == "2":
            display_customers()
            
        elif choice == "3":
            sender_acc_id = input("Enter Sender Account ID: ")
            receiver_acc_id = input("Enter Receiver Account ID: ")
            amount = float(input("Enter Transaction Amount: "))
            transaction(sender_acc_id, receiver_acc_id, amount)
            
        elif choice == "4":
            print("Thank you for using the Bank Management System.")
            print("-------------------------------------------------------------------------------------")
            break
            
        else:
            print("Invalid choice. Please try again.")
        print("-------------------------------------------------------------------------------------")
        time.sleep(1)

if __name__ == "__main__":
    main()
