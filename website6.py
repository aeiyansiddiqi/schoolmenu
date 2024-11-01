import re
import psycopg2
from psycopg2 import sql

# Function to read the menu from a text file
def read_menu_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

# Read the menu text from the file
menu_text = read_menu_from_file('menu_output.txt')

# Function to extract menu for a given day
def extract_menu(day: str):
    # Create regex pattern for the given day, allowing for full or abbreviated month names
    pattern = rf"{day},? (?:October|November|Oct|Nov) \d+\n(?:Mom's Kitchen & Nature's Best\n)?(.*?)(?=\n(?:Infusion|$))"
    items = re.search(pattern, menu_text, re.DOTALL)

    # Check if we found matches
    if items:
        # Extract the menu items for the day
        menu = items.group(1).strip()
        
        # Store items in a list, line by line
        day_menu = [item.strip() for item in menu.split('\n') if item.strip()]
        
        return day_menu
    else:
        return None

# List of days to extract menus for
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",        # replace with your PostgreSQL host
    database="your_database", # replace with your PostgreSQL database
    user="your_username",     # replace with your PostgreSQL username
    password="your_password"  # replace with your PostgreSQL password
)
cur = conn.cursor()

# Create table if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS weekly_menu (
        id SERIAL PRIMARY KEY,
        day VARCHAR(10) NOT NULL,
        item TEXT NOT NULL
    );
''')
conn.commit()

# Insert daily menu into PostgreSQL table
for day in days:
    menu_items = extract_menu(day)
    if menu_items:
        for item in menu_items:
            cur.execute(
                'INSERT INTO weekly_menu (day, item) VALUES (%s, %s)',
                (day, item)
            )
        conn.commit()
    else:
        print(f"No items found for {day}'s menu.\n")

# Close the connection
cur.close()
conn.close()
