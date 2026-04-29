import psycopg2
import csv
import os
import json
from datetime import datetime

 
conn = psycopg2.connect(
    host="localhost",
    dbname="postgres",
    user="postgres",                                 #Here i dedicate my database info
    password="1234",
    port="5555"
)
cur = conn.cursor()

                                                                #there starts json part 

def export_to_json(file_path="C:\TT\Python\contacts_export.json"):
    # Собираем данные: контакты + их телефоны + название группы
    query = """
        SELECT c.id, c.name, c.email, c.birthday, g.name as group_name,
               ARRAY_AGG(p.phone || ':' || p.type) as phone_list
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        GROUP BY c.id, g.name
    """
    cur.execute(query)
    rows = cur.fetchall()
    
    data = []
    for row in rows:
        data.append({
            "name": row[1],
            "email": row[2],
            "birthday": str(row[3]) if row[3] else None,
            "group": row[4],
            "phones": row[5] if row[5][0] is not None else []
        })
    
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data exported to {file_path}")

def import_from_json(file_path):
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден!")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        contacts = json.load(f)
    
    for c in contacts:
        cur.execute("SELECT id FROM contacts WHERE name = %s", (c['name'],))
        exists = cur.fetchone()
        
        if exists:
            choice = input(f"Контакт '{c['name']}' уже существует. Пропустить или Перезаписать? (s/o): ").lower()
            if choice == 's': continue
            cur.execute("DELETE FROM contacts WHERE id = %s", (exists[0],))

        
        group_name = c.get('group', 'Other')
        cur.execute(
            "INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO UPDATE SET name=EXCLUDED.name RETURNING id",
            (group_name,)
        )
        group_id = cur.fetchone()[0]

       
        cur.execute(
            "INSERT INTO contacts (name, email, birthday, group_id) VALUES (%s, %s, %s, %s) RETURNING id",
            (c['name'], c.get('email'), c.get('birthday'), group_id)
        )
        contact_id = cur.fetchone()[0]

        
        for p_entry in c.get('phones', []):
            if ':' in p_entry:
                phone_val, phone_type = p_entry.split(':', 1)
            elif ' (' in p_entry:
                phone_val = p_entry.split(' (')[0]
                phone_type = p_entry.split(' (')[1].replace(')', '')
            else:
                phone_val = p_entry
                phone_type = 'mobile' # тип по умолчанию

            cur.execute(
                "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                (contact_id, phone_val.strip(), phone_type.strip())
            )
    
    conn.commit()
    


 
                                               #search and view part
                                                 
def paginated_view():
    limit = 5
    page = 1
    while True:
        offset = (page - 1) * limit
        cur.execute("SELECT name, email FROM contacts ORDER BY name LIMIT %s OFFSET %s", (limit, offset))
        rows = cur.fetchall()
        
        print(f"\n--- Page {page} ---")
        for r in rows: print(f"Name: {r[0]} | Email: {r[1]}")
        
        cmd = input("\n[n] Next, [p] Prev, [q] Quit: ").lower()
        if cmd == 'n': page += 1
        elif cmd == 'p' and page > 1: page -= 1
        elif cmd == 'q': break

def advanced_search():
    print("1 - Filter by Group\n2 - Search by Email\n3 - Search All (Name/Phone/Email)")
    choice = input("Select: ")
    
    if choice == "1":
        g_name = input("Enter group name: ")
        cur.execute("SELECT c.name FROM contacts c JOIN groups g ON c.group_id = g.id WHERE g.name = %s", (g_name,))
    elif choice == "2":
        email = input("Enter email pattern (e.g. gmail): ")
        cur.execute("SELECT name, email FROM contacts WHERE email ILIKE %s", (f"%{email}%",))
    elif choice == "3":
        pattern = input("Search everywhere: ")
        # Вызов новой функции из задания 3.4
        cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    
    for row in cur.fetchall(): print(row)

                                                       #procedures part

def call_procedures():
    print("1 - Add phone to contact\n2 - Move contact to group")
    choice = input("Select: ")
    
    if choice == "1":
        name = input("Contact name: ")
        phone = input("Phone: ")
        ptype = input("Type (home/work/mobile): ")
        cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
    elif choice == "2":
        name = input("Contact name: ")
        group = input("New group name: ")
        cur.execute("CALL move_to_group(%s, %s)", (name, group))
    
    conn.commit()
    


def insert_from_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            cur.execute(
                "INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO UPDATE SET name=EXCLUDED.name RETURNING id",
                (row['group'],)
            )
            group_id = cur.fetchone()[0]

            
            cur.execute(
                """INSERT INTO contacts (name, email, birthday, group_id) 
                   VALUES (%s, %s, %s, %s) RETURNING id""",
                (row['name'], row['email'], row['birthday'], group_id)
            )
            contact_id = cur.fetchone()[0]

           
            cur.execute(
                "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
                (contact_id, row['number'], row['phone_type'])
            )
            
        conn.commit()
        


def add_extended_contact():
    name = input("Nane: ")
    email = input("Email: ")
    birthday = input("Birth date (YYYY-MM-DD): ")
    group_name = input("Group (Family, Work, Friend, Other): ")
    
    
    phone = input("Number: ")
    phone_type = input("Type (home, work, mobile): ")

    try:
        
        cur.execute(
            "INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO UPDATE SET name=EXCLUDED.name RETURNING id",
            (group_name,)
        )
        group_id = cur.fetchone()[0]

        
        cur.execute(
            """INSERT INTO contacts (name, email, birthday, group_id) 
               VALUES (%s, %s, %s, %s) RETURNING id""",
            (name, email, birthday, group_id)
        )
        contact_id = cur.fetchone()[0]

        
        cur.execute(
            "INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)",
            (contact_id, phone, phone_type)
        )

        conn.commit()
        

    except Exception as e:
        conn.rollback()
        print(f"Errrrror: {e}")



#menu part


def menu():
    while True:
        print("\n--- EXTENDED PHONE BOOK ---")
        print("1 - Import from CSV (Updated)")
        print("2 - Add Contact (Basic)")
        print("3 - Advanced Search & Filter")
        print("4 - Paginated Navigation")
        print("5 - Procedures (Add Phone / Move Group)")
        print("6 - Export to JSON")
        print("7 - Import from JSON")
        print("0 - Exit")

        choice = input("Select: ")

        if choice == "1":
            insert_from_csv("C:\TT\Python\contacts.csv")
            print("CSV logic should be updated to handle email/birthday/group")
        elif choice == "2":
            add_extended_contact()
            pass 
        elif choice == "3":
            advanced_search()
        elif choice == "4":
            paginated_view()
        elif choice == "5":
            call_procedures()
        elif choice == "6":
            export_to_json()
        elif choice == "7":
            import_from_json("C:/TT/Python/import.json")
        elif choice == "0":
            break

    cur.close()
    conn.close()

if __name__ == "__main__":
    menu()