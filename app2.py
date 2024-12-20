from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('weekly_menu.db')
    conn.row_factory = sqlite3.Row  # Allows us to fetch rows as dictionaries
    return conn

# Route to retrieve the menu for a specific day
@app.route('/menu/<day>', methods=['GET'])
def get_menu_for_day(day):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT meal_time, item FROM menu WHERE day = ?
    ''', (day,))
    items = cursor.fetchall()
    conn.close()

    # Structure the items by meal time
    menu = {}
    for item in items:
        meal_time = item['meal_time']
        if meal_time not in menu:
            menu[meal_time] = []
        menu[meal_time].append(item['item'])

    if menu:
        return jsonify({day: menu})
    else:
        return jsonify({"error": f"No menu found for {day}"}), 404

# Route to add a new menu item for a specific day
@app.route('/menu', methods=['POST'])
def add_menu_item():
    data = request.json
    day = data.get('day')
    meal_time = data.get('meal_time')
    item = data.get('item')

    if not all([day, meal_time, item]):
        return jsonify({"error": "Day, meal_time, and item are required"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO menu (day, meal_time, item) 
        VALUES (?, ?, ?)
    ''', (day, meal_time, item))
    conn.commit()
    conn.close()

    return jsonify({"message": "Menu item added successfully!"}), 201


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
