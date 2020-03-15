from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/product'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Product(db.Model):
    __tablename__ = 'product'
    
    ProductID = db.Column(db.Integer, primary_key=True)
    CustEmail = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(50), nullable=False)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    Birthdate = db.Column(db.DateTime, nullable=False)
    Gender = db.Column(db.String(1), nullable=False)
    MobileNum = db.Column(db.Integer, nullable=False)
    Address = db.Column(db.String(100), nullable=False)
    UnitNum = db.Column(db.String(10), nullable=False)
    Country = db.Column(db.String(100), nullable=False)
    RegistrationDate = db.Column(db.DateTime, nullable=False)
    NewsletterSubscription = db.Column(db.String(1), nullable=False)

    def __init__(self, CustID, CustEmail, Password, FirstName, LastName, Birthdate, Gender, MobileNum, Address, UnitNum, PostalCode, Country, RegistrationDate, NewsletterSubscription):
        self.CustID = CustID
        self.CustEmail = CustEmail
        self.Password = Password
        self.FirstName = FirstName
        self.LastName = LastName
        self.Birthdate = Birthdate
        self.Gender = Gender
        self.MobileNum = MobileNum
        self.Address = Address
        self.UnitNum = UnitNum
        self.Country = Country
        self.RegistrationDate = RegistrationDate
        self.NewsletterSubscription = NewsletterSubscription

    def json(self):
        return {"CustID": self.CustID, 
                "CustEmail": self.CustEmail,
                "Password": self.Password,
                "FirstName": self.FirstName, 
                "LastName": self.LastName,
                "Birthdate": self.Birthdate,
                "Gender": self.Gender,
                "MobileNum": self.MobileNum,
                "Address": self.Address,
                "UnitNum": self.UnitNum,
                "Country": self.Country,
                "RegistrationDate": self.RegistrationDate,
                "NewsletterSubscription": self.NewsletterSubscription
                }


@app.route("/product")
def get_all():
    return jsonify({"customers": [product.json() for product in Customer.query.all()]})


@app.route("/product/<string:CustEmail>", methods=['GET'])
def find_by_CustEmail(CustEmail):
    product = Customer.query.filter_by(CustEmail=CustEmail).first()
    if product:
        return jsonify(product.json())
    return jsonify({"message": "CustEmail not found."}), 404


@app.route("/product/<string:CustEmail>", methods=['POST'])
def create_customer(CustEmail):
    if (Customer.query.filter_by(CustEmail=CustEmail).first()):
        return jsonify({"message": "Customer'{}' already exists.".format(CustEmail)}), 400

    data = request.get_json()
    product = Customer(CustEmail, **data)

    try:
        db.session.add(product)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating product."}), 500

    return jsonify(product.json()), 201

@app.route("/product/<string:CustEmail>", methods=['PUT'])
def update_customer(CustEmail):
    product = Customer.query.get(CustEmail)
    CustEmail = request.json['CustEmail']
    Password = request.json['Password']

    product.CustEmail = CustEmail
    product.Password = Password

    db.session.commit()
    return customer_schema.jsonify(product)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
