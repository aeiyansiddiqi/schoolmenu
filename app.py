from flask import Flask, jsonify, request
from flask_sqlalchemy import flask_sqlalchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_db_user:your_db_password@localhost/your_db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(5,2), nullable=False)
    image_url = db.Column(db.String, nullable = True)


#Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

#define a route to get all menu items
@app.route('/menu', methods=['GET'])
    items = MenuItem.query.all()
    return jsonify([{
        'id': item.id, 
        'name': item.name, 
        'description': item.description, 
        'price': str(item.price), #Convert decimal to string
        'image_url': item.image_url
    }   for item in items])


# define a route to add a new menu item
@app.route('/menu', methods=['POST'])
def add_menu_item():
    data = request.json
    new_item = MenuItem(
        name=data['name'], 
        description = data['description'], 
        price = data['price'], 
        image_url = data['image_url']

    )
    db.session.add(new_item)
    db.session.commit()
    return jsonify({'message': 'Menu item added!'}), 201

if __name__ = '__main__':
    app.run(debug=True)