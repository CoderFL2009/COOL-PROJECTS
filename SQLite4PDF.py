import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import inch


# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('people.db')
cursor = conn.cursor()


# Create a table called 'people' with columns for name, age, and favorite band
cursor.execute('''
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    favorite_band TEXT
)
''')

# Function to add a new person to the database
def add_person(name, age, favorite_band):
    cursor.execute('''
    INSERT INTO people (name, age, favorite_band)
    VALUES (?, ?, ?)
    ''', (name, age, favorite_band))
    conn.commit()
    print(f"{name} has been added to the database.")

# Function to retrieve and display all people in the database
def show_all_people():
    cursor.execute('SELECT * FROM people')
    rows = cursor.fetchall()
    print("\nPeople in the database: ")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}, Favorite Band: {row[3]}")
    print("\n")

# Function to remove a person from the database by ID
def remove_person(person_id):
    cursor.execute('DELETE FROM people WHERE id = ?',  (person_id,))
    conn.commit()
    print(f"Person with ID {person_id} has been removed from the database.")

def export_to_pdf():
    cursor.execute('SELECT * FROM people')
    rows = cursor.fetchall()

    pdf_file = "people_database.pdf"
    pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

    data = [["ID", "Name", "Age", "Favorite Band"]]
    for row in rows:
        data.append(list(row))


    table = Table(data, colWidths=[0.5 * inch, 1.5 * inch, 1 * inch, 2 * inch])

    table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.blue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.green),
        ('GRID', (0, 0), (-1, -1), 1, colors.cyan),
    ]))

    elements = [table]
    pdf.build(elements)
    print(f"Data has been written to {pdf_file}")

# Main program loop
while True:
    print("Options:")
    print("1. Add a new person")
    print("2. Display all people")
    print("3. Remove a person")
    print("4. Export to PDF ")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        # Get user input
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        favorite_band = input("Enter Favorite Band: ")
        # Add the person to the database
        add_person(name, age, favorite_band)

    elif choice == '2':
        # Display all entries in the database
        show_all_people()
    elif choice == '3':
        # Remove a person by ID
        show_all_people() #Show current entries for reference
        try:
            person_id = int(input("Enter thr ID of the person to remove: "))
            remove_person(person_id)
        except ValueError:
            print("Invalid ID Number")

    elif choice == '4':
        export_to_pdf()

    elif choice == '5':
        print("Goodbye")
        break
    else:
        print("Invalid choice, try again")
# Exit the program


# Close the database connection
conn.close()