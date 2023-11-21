from flask import Flask, jsonify, render_template, request
from sqlalchemy import Integer, String, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, DeclarativeBase, mapped_column
from flask_sqlalchemy import SQLAlchemy


# create the db object using the SQLAlchemy constructor
# Pass a subclass of either DeclarativeBase or DeclarativeBaseNoMeta
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'

# initialize the app with the extension
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    ''' A table to hold data on coffee shops '''
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[String] = mapped_column(
        String(250), unique=True, nullable=False)
    map_url: Mapped[String] = mapped_column(String(500), nullable=False)
    img_url: Mapped[String] = mapped_column(String(500), nullable=False)
    location: Mapped[String] = mapped_column(String(250), nullable=False)
    seats: Mapped[String] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[Boolean] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[Boolean] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[Boolean] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[Boolean] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[String] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        ''' Makes a dictionary from table column names and values so
            we can pass it to jsonify later and return json'''
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            # Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary
        # return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    # create_all does not update tables if they are already in the database
    db.create_all()


@app.route("/")
def home():
    ''' Home page with link to API docs '''
    return render_template("index.html")


@app.route('/random')
def random():
    ''' Gets a random cafe and returns a json object'''
    rand_cafe = Cafe.query.order_by(func.random()).first()
    cafe_json = jsonify(
        id=rand_cafe.id,
        name=rand_cafe.name,
        map_url=rand_cafe.map_url,
        img_url=rand_cafe.img_url,
        location=rand_cafe.location,
        has_sockets=rand_cafe.has_sockets,
        has_toilet=rand_cafe.has_toilet,
        has_wifi=rand_cafe.has_wifi,
        can_take_calls=rand_cafe.can_take_calls,
        seats=rand_cafe.seats,
        coffee_price=rand_cafe.coffee_price
    )
    return cafe_json


# HTTP GET - Read Record
@app.route('/all')
def all_cafes():
    ''' Returns json with all the cafes '''
    result = db.session.execute(
        db.select(Cafe).order_by(Cafe.id)).scalars().all()
    cafe_list = [cafe.to_dict() for cafe in result]
    return jsonify(cafes=cafe_list)


@app.route('/search')
def search():
    ''' Finds a cafe based on id in query string url like:/search?loc=Peckham
        returns json'''
    location_str = request.args.get('loc')
    print(type(location_str))

    result = db.session.execute(
        db.select(Cafe).where(Cafe.location == location_str.title()))
    cafes = result.scalars().all()
    if len(cafes) == 0:
        return {"error": {"Not Found": "Sorry, we don't have a cafe at that location."}}

    cafe_list = [cafe.to_dict() for cafe in cafes]
    return jsonify(cafes=cafe_list)

# HTTP POST - Create Record


@app.route('/add', methods=['POST'])
def add_new_cafe():
    ''' Takes a post request with cafe data and add it to database 
        returns json '''
    if request.method == 'POST':
        new_cafe = Cafe(
            name=request.form.get('name'),
            map_url=request.form.get('map_url'),
            img_url=request.form.get('img_url'),
            location=request.form.get('location'),
            has_sockets=bool(request.form.get('sockets')),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully add the new cafe."})

# HTTP PUT/PATCH - Update Record


@app.route('/update-price/<int:id>', methods=['PATCH'])
def update_price(id):
    ''' Updates price on patch request with url string: /update-price/2?price=£3.20 '''
    if request.method == 'PATCH':
        price = request.args.get('price')
        cafe = db.session.get(Cafe, id)
        if cafe:
            cafe.coffee_price = price
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."})
        return jsonify(error={"Not Found": "That cafe id is not in the database."}), 404


# HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    ''' Deletes cafe based on id if api-key is correct returns json
        success or error'''
    if request.method == 'DELETE':
        if request.args.get('api-key') == "TopSecretAPIKey":
            cafe = db.session.get(Cafe, cafe_id)
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": f"Successfully deleted cafe:{cafe.name}"})
        return jsonify(error={'Not Allowed': "You are not authorised to delete"}), 403


if __name__ == '__main__':
    app.run(debug=True)
