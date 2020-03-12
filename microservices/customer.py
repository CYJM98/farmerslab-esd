from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/customer'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Customer(db.Model):
    __tablename__ = 'customer'
    
    CustID = db.Column(db.Integer, primary_key=True)
    CustEmail = db.Column(db.String(100), nullable=False)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    Birthdate = db.Column(db.DateTime, nullable=False)
    Gender = db.Column(db.String(1), nullable=False)
    MobileNum = db.Column(db.Integer, nullable=False)
    Address = db.Column(db.String(100), nullable=False)
    UnitNum = db.Column(db.String(10), nullable=False)
    Country = db.Column(db.String(100), nullable=False)
    RegistrationDate = db.Column(db.DateTime, nullable=False)
    Username = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(50), nullable=False)

    def __init__(self, CustID, CustEmail, FirstName, LastName, Birthdate, Gender, MobileNum, Address, UnitNum, PostalCode, Country, RegistrationDate, Username, Password):
        self.CustID = CustID
        self.CustEmail = CustEmail
        self.FirstName = FirstName
        self.LastName = LastName
        self.Birthdate = Birthdate
        self.Gender = Gender
        self.MobileNum = MobileNum
        self.Address = Address
        self.UnitNum = UnitNum
        self.Country = Country
        self.RegistrationDate = RegistrationDate
        self.Username = Username
        self.Password = Password

    def json(self):
        return {"CustID": self.CustID, 
                "CustEmail": self.CustEmail, 
                "FirstName": self.FirstName, 
                "LastName": self.LastName,
                "Birthdate": self.Birthdate,
                "Gender": self.Gender,
                "MobileNum": self.MobileNum,
                "Address": self.Address,
                "UnitNum": self.UnitNum,
                "Country": self.Country,
                "RegistrationDate": self.RegistrationDate,
                "Username": self.Username,
                "Password": self.Password
                }


@app.route("/customer")
def get_all():
    return jsonify({"customers": [customer.json() for customer in Customer.query.all()]})


@app.route("/customer/<string:Username>", methods=['GET'])
def find_by_Username(Username):
    customer = Customer.query.filter_by(Username=Username).first()
    if customer:
        return jsonify(customer.json())
    return jsonify({"message": "Username not found."}), 404


@app.route("/customer/<string:Username>", methods=['POST'])
def create_customer(Username):
    if (Customer.query.filter_by(Username=Username).first()):
        return jsonify({"message": "Customer'{}' already exists.".format(Username)}), 400

    data = request.get_json()
    customer = Customer(Username, **data)

    try:
        db.session.add(customer)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating customer."}), 500

    return jsonify(customer.json()), 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
