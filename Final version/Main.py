import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='urlakalangu',
    database='TechnoSparkz'
)
skm = mydb.cursor()

# Utility function to create the cart table
def create_cart_table():
    skm.execute("CREATE TABLE IF NOT EXISTS cart (Sno INT, Brand VARCHAR(255), Model VARCHAR(255), Price INT);")
    print("Cart table ready.")

# Function to add an item to the cart
def add_to_cart(sno, table_name):
    skm.execute(f"SELECT Sno, Brand, Model, Price FROM {table_name} WHERE Sno = %s", (sno,))
    item = skm.fetchone()
    if item:
        skm.execute("INSERT INTO cart (Sno, Brand, Model, Price) VALUES (%s, %s, %s, %s)", item)
        mydb.commit()
        print(f"Item '{item[2]}' added to cart.")  # Item's Model
    else:
        print("Error: Item not found.")

# Function to display the cart
def view_cart():
    skm.execute("SELECT * FROM cart;")
    cart_items = skm.fetchall()
    if not cart_items:
        print("Your cart is empty.")
    else:
        print("\nYour Cart:")
        print("Sno\tBrand\t\tModel\t\tPrice")
        for item in cart_items:
            print(f"{item[0]}\t{item[1]}\t{item[2]}\t₹{item[3]}")
        total = sum(item[3] for item in cart_items)
        print(f"Total: ₹{total}")

# Customer flow
def customer_flow():
    create_cart_table()
    categories = {
        1: "Adapter",
        2: "Monitor",
        3: "Keyboard",
        4: "Mouse",
        5: "Headphone"
    }

    while True:
        print("\nAvailable Categories:")
        for key, value in categories.items():
            print(f"{key}. {value}")

        category_choice = int(input("Choose a category (1-5): "))
        if category_choice in categories:
            table_name = categories[category_choice]
            skm.execute(f"SELECT * FROM {table_name};")
            items = skm.fetchall()
            print("\nProducts Available:")
            if table_name == "Adapter":
                print("Sno\tBrand\t\tModel\t\tOutput Power\tPort Model\tPrice")
                for item in items:
                    print(f"{item[0]}\t{item[1]}\t{item[2]}\t{item[3]}\t{item[4]}\t₹{item[5]}")
            else:
                print("Sno\tBrand\t\tModel\t\tPrice")
                for item in items:
                    print(f"{item[0]}\t{item[1]}\t{item[2]}\t₹{item[3]}")

            sno = int(input("Enter the Serial Number (Sno) of the product to add to cart: "))
            add_to_cart(sno, table_name)
        else:
            print("Invalid category choice!")

        another = input("Would you like to add more items? (yes/no): ").strip().lower()
        if another != 'yes':
            break

    view_cart()
    checkout = input("Would you like to checkout? (yes/no): ").lower()
    if checkout == "yes":
        print("Thank you for shopping with us!")
        skm.execute("DELETE FROM cart;")  # Clear cart after checkout
        mydb.commit()

# Admin flow
def admin_flow():
    username = input("Enter username: ")
    password = input("Enter password: ")
    skm.execute("SELECT * FROM admin WHERE Username = %s AND Password = %s", (username, password))
    admin = skm.fetchone()
    if admin:
        print(f"Welcome, {admin[1]}!")
        while True:
            print("\nAdmin Menu:")
            print("1. View Stock")
            print("2. Exit")
            choice = int(input("Choose an option: "))
            if choice == 1:
                print("\nAvailable Stock Tables:")
                stock_tables = {
                    1: "Adapter",
                    2: "Monitor",
                    3: "Keyboard",
                    4: "Mouse",
                    5: "Headphone"
                }
                for key, value in stock_tables.items():
                    print(f"{key}. {value}")
                print("6. Exit")
                table_choice = int(input("Choose a stock table to view: "))
                if table_choice in stock_tables:
                    table_name = stock_tables[table_choice]
                    skm.execute(f"SELECT * FROM {table_name};")
                    items = skm.fetchall()
                    print(f"\n{table_name} Stock:")
                    for item in items:
                        print(item)
                elif table_choice == 6:
                    break
                else:
                    print("Invalid choice!")
            elif choice == 2:
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
    else:
        print("Invalid username or password!")

# Main Program
if __name__ == "__main__":
    print("\nWelcome to TechnoSparkz!")
    print("Are you:")
    print("1. Admin")
    print("2. Customer")
    role = int(input("Choose your role (1 or 2): "))
    if role == 1:
        admin_flow()
    elif role == 2:
        customer_flow()
    else:
        print("Invalid role selected!")
