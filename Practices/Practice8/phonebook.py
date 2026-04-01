import psycopg2
import csv

# ---------- CONNECTION ----------
conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",
    password="1234",
    port = "5555"
)
cur = conn.cursor()

#====================================================================================================================================================
def insert_from_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header
        
        data = []
        for row in reader:
            data.append((row[1], row[2], row[3]))  # skip id

        cur.executemany(
            "INSERT INTO phone_book (name, age, number) VALUES (%s, %s, %s)",
            data
        )
        conn.commit()
        print("CSV data inserted!")

#======================================================================================================================
def insert_from_console():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    number = input("Enter phone: ")

    cur.execute(
        "INSERT INTO phone_book (name, age, number) VALUES (%s, %s, %s)",
        (name, age, number)
    )
    conn.commit()
    print("Contact added!")

#========================================================================================================================
def update_contact():
    name = input("Enter name to update: ")
    choice = input("Update (1) Name or (2) Phone: ")

    if choice == "1":
        new_name = input("Enter new name: ")
        cur.execute(
            "UPDATE phone_book SET name = %s WHERE name = %s",
            (new_name, name)
        )
    elif choice == "2":
        new_number = input("Enter new phone: ")
        cur.execute(
            "UPDATE phone_book SET number = %s WHERE name = %s",
            (new_number, name)
        )

    conn.commit()
    print("Updated!")

#============================================================================================================================
def query_contacts():
    print("1 - Show all")
    print("2 - Search by name")
    print("3 - Search by phone prefix")

    choice = input("Choose: ")

    if choice == "1":
        cur.execute("SELECT * FROM phone_book")

    elif choice == "2":
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM phone_book WHERE name ILIKE %s",
            (f"%{name}%",)
        )

    elif choice == "3":
        prefix = input("Enter prefix: ")
        cur.execute(
            "SELECT * FROM phone_book WHERE number LIKE %s",
            (f"{prefix}%",)
        )

    rows = cur.fetchall()
    for row in rows:
        print(row)

#=====================================================================================================================
def delete_contact():
    print("1 - Delete by name")
    print("2 - Delete by phone")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute(
            "DELETE FROM phone_book WHERE name = %s",
            (name,)
        )

    elif choice == "2":
        number = input("Enter phone: ")
        cur.execute(
            "DELETE FROM phone_book WHERE number = %s",
            (number,)
        )

    conn.commit()
    print("Deleted!")

#====================================================================================================================================================
def menu():
    while True:
        print("\n--- PHONE BOOK ---")
        print("1 - Insert from CSV")
        print("2 - Add contact")
        print("3 - Update contact")
        print("4 - Query contacts")
        print("5 - Delete contact")
        print("0 - Exit")

        choice = input("Select: ")

        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            query_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "0":
            break

    cur.close()
    conn.close()


menu()