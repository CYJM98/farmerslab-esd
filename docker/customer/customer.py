from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/customer'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Customer(db.Model):
    __tablename__ = 'customer'
    
    CustEmail = db.Column(db.String(100), primary_key=True)
    Password = db.Column(db.String(50), nullable=False)
    FirstName = db.Column(db.String(50), nullable=False)
    LastName = db.Column(db.String(50), nullable=False)
    Birthdate = db.Column(db.String(20), nullable=False)
    Gender = db.Column(db.String(1), nullable=False)
    MobileNum = db.Column(db.Integer, nullable=False)
    Address = db.Column(db.String(100), nullable=False)
    UnitNum = db.Column(db.String(10), nullable=False)
    PostalCode = db.Column(db.String(10), nullable=False)
    Country = db.Column(db.String(100), nullable=False)
    RegistrationDate = db.Column(db.DateTime, nullable=False)
    NewsletterSubscription = db.Column(db.String(1), nullable=False)

    def __init__(self, CustEmail, Password, FirstName, LastName, Birthdate, Gender, MobileNum, Address, UnitNum, PostalCode, Country, RegistrationDate, NewsletterSubscription):
        self.CustEmail = CustEmail
        self.Password = Password
        self.FirstName = FirstName
        self.LastName = LastName
        self.Birthdate = Birthdate
        self.Gender = Gender
        self.MobileNum = MobileNum
        self.Address = Address
        self.UnitNum = UnitNum
        self.PostalCode = PostalCode
        self.Country = Country
        self.RegistrationDate = RegistrationDate
        self.NewsletterSubscription = NewsletterSubscription

    def json(self):
        return {"CustEmail": self.CustEmail,
                "Password": self.Password,
                "FirstName": self.FirstName, 
                "LastName": self.LastName,
                "Birthdate": self.Birthdate,
                "Gender": self.Gender,
                "MobileNum": self.MobileNum,
                "Address": self.Address,
                "UnitNum": self.UnitNum,
                "PostalCode": self.PostalCode,
                "Country": self.Country,
                "RegistrationDate": self.RegistrationDate,
                "NewsletterSubscription": self.NewsletterSubscription
                }

@app.route("/customer")
def get_all():
    return jsonify({"customers": [customer.json() for customer in Customer.query.all()]})


@app.route("/customer/<string:CustEmail>", methods=['GET'])
def find_by_CustEmail(CustEmail):
    customer = Customer.query.filter_by(CustEmail=CustEmail).first()
    if customer:
        return jsonify(customer.json())
    return jsonify({"message": "CustEmail not found."}), 404

@app.route("/customer", methods=['POST'])
def create_customer():
    
    data = request.get_json()
    CustEmail = data["CustEmail"]

    if (Customer.query.filter_by(CustEmail=CustEmail).first()):
        return jsonify({"message": "Customer'{}' already exists.".format(CustEmail)}), 400
    
    customer = Customer(**data)
    
    try:
        db.session.add(customer)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating customer."}), 500

    return jsonify(customer.json()), 201

@app.route("/customer/<string:CustEmail>", methods=['PUT'])
def update_customer(CustEmail):
    customer = Customer.query.get(CustEmail)
    CustEmail = request.json['CustEmail']
    Password = request.json['Password']

    customer.CustEmail = CustEmail
    customer.Password = Password

    db.session.commit()
    return customer_schema.jsonify(customer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

# 1) set dbURL=mysql+mysqlconnector://root@localhost:3306/customer
# python customer.py
# pip install -r requirements.txt
# 2) docker build -t ycm98/customer:1.0.0 .
# View Images: docker images
# Remove Image: docker rmi <image id>
# 3) docker run -p 5000:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/customer ycm98/customer:1.0.0
# 4) docker run -p 5900:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/customer ycm98/customer:1.0.0	
# Container (Start): docker start <containerid> (Stop): docker stop 
# (Check): docker ps (Logs): docker logs (Remove) docker rm <containerid>