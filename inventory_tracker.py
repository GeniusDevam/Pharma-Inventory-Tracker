import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('pharmacy.db')
c = conn.cursor()

# Create a table for inventory
c.execute('''CREATE TABLE IF NOT EXISTS inventory
             (id INTEGER PRIMARY KEY, medication_name TEXT, quantity INTEGER, expiration_date TEXT)''')

# Function to add new medication
def add_medication(name, quantity, exp_date):
    c.execute("INSERT INTO inventory (medication_name, quantity, expiration_date) VALUES (?, ?, ?)", 
              (name, quantity, exp_date))
    conn.commit()

# Function to update stock
def update_stock(name, quantity):
    c.execute("UPDATE inventory SET quantity = ? WHERE medication_name = ?", 
              (quantity, name))
    conn.commit()

# Function to view inventory
def view_inventory():
    c.execute("SELECT * FROM inventory")
    inventory = c.fetchall()
    for row in inventory:
        print(row)

# Main menu
def main():
    while True:
        print("\nPharmacy Inventory Tracker")
        print("1. Add Medication")
        print("2. Update Stock")
        print("3. View Inventory")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter medication name: ")
            quantity = int(input("Enter quantity: "))
            exp_date = input("Enter expiration date (YYYY-MM-DD): ")
            add_medication(name, quantity, exp_date)
        elif choice == '2':
            name = input("Enter medication name to update: ")
            quantity = int(input("Enter new quantity: "))
            update_stock(name, quantity)
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

    conn.close()

if __name__ == "__main__":
    main()
