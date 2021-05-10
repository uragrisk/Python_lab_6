from enum import Enum, auto

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/ship-manager'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class SurfaceType(Enum):
    WATER = "Water"
    GROUNG = "Ground"

class MovementType(Enum):
   PROPELLERS = "propellers"
   WINGS = "wings"
   SAILS = "sails"

class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(16), nullable=False)
    tonnage: float = db.Column(db.Float(8), nullable=False)
    max_speed: int = db.Column(db.Integer(), nullable=False)
    fuel_per_100miles: float = db.Column(db.Float(6), nullable=False)
    movement_surface: SurfaceType = db.Column(db.Enum(SurfaceType), nullable=False)
    movement_type: MovementType = db.Column(db.Enum(MovementType), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return '<Ship %r>' % self.id

@app.route('/',  methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        tonnage = request.form['tonnage']
        max_speed = request.form['max_speed']
        fuel_per_100miles = request.form['fuel_per_100miles']
        movement_surface = request.form['movement_surface']
        movement_type = request.form['movement_type']
        new_ship = Ship(name=name,
                        tonnage=tonnage,
                        max_speed=max_speed,
                        fuel_per_100miles=fuel_per_100miles,
                        movement_surface=movement_surface,
                        movement_type=movement_type)

        try:
            db.session.add(new_ship)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your ship'

    else:
        ships = Ship.query.all()
        return render_template('index.html', ships=ships)

@app.route('/delete/<int:id>')
def delete(id):
    ship_to_delete = Ship.query.get_or_404(id)

    try:
        db.session.delete(ship_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting a that ship'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    ship = Ship.query.get_or_404(id)

    if request.method == 'POST':
        ship.name = request.form['name']
        ship.tonnage = request.form['tonnage']
        ship.max_speed = request.form['max_speed']
        ship.fuel_per_100miles = request.form['fuel_per_100miles']
        ship.movement_surface = request.form['movement_surface']
        ship.movement_type = request.form['movement_type']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your ship'

    else:
        return render_template('update.html', ship=ship)





#
# @app.route('/delete/<int:id>')
# def delete(id):
#     loom_to_delete = HandLoom.query.get_or_404(id)
#
#     try:
#         db.session.delete(loom_to_delete)
#         db.session.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deleting a that loom'
#
#
# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     loom = HandLoom.query.get_or_404(id)
#
#     if request.method == 'POST':
#         loom.origin_country = request.form['origin_country']
#         loom.price = request.form['price']
#         loom.power_in_watts = request.form['power_in_watts']
#         loom.width_of_the_formed_tissue = request.form['width_of_the_formed_tissue']
#         loom.material_of_the_produced_fabric = request.form['material_of_the_produced_fabric']
#         loom.manufacture_century = request.form['manufacture_century']
#         loom.status = request.form['status']
#
#         try:
#             db.session.commit()
#             return redirect('/')
#         except:
#             return 'There was an issue updating your loom'
#
#     else:
#         return render_template('update.html', loom=loom)
#
#
if __name__ == '__main__':
    app.run(debug=True)
