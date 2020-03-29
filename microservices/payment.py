from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/payment'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Payment(db.Model):
    __tablename__ = 'payment'
    
    PaymentID = db.Column(db.Integer, primary_key=True)
    OrderID = db.Column(db.Integer, nullable=False)
    PaymentAmount = db.Column(db.Float(precision=2), nullable=False)
    PaymentDateTime = db.Column(db.DateTime, nullable=False)
    PaymentType = db.Column(db.String(20), nullable=False)

    def __init__(self, PaymentID, OrderID, PaymentAmount, PaymentDateTime, PaymentType):
        self.PaymentID = PaymentID
        self.OrderID = OrderID
        self.PaymentAmount = PaymentAmount
        self.PaymentDateTime = PaymentDateTime
        self.PaymentType = PaymentType
        
    def json(self):
        return {"PaymentID": self.PaymentID,
                "OrderID": self.OrderID,
                "PaymentAmount": self.PaymentAmount, 
                "PaymentDateTime": self.PaymentDateTime,
                "PaymentType": self.PaymentType
                }

@app.route("/payment")
def get_all():
    return jsonify({"payments": [payment.json() for payment in Payment.query.all()]})


@app.route("/payment/<int:PaymentID>", methods=['GET'])
def find_by_PaymentID(PaymentID):
    payment = Payment.query.filter_by(PaymentID=PaymentID).first()
    if payment:
        return jsonify(payment.json())
    return jsonify({"message": "PaymentID not found."}), 404

@app.route("/payment", methods=['POST'])
def create_payment():
    
    data = request.get_json()
    PaymentID = data["PaymentID"]

    if (Payment.query.filter_by(PaymentID=PaymentID).first()):
        return jsonify({"message": "Payment'{}' already exists.".format(PaymentID)}), 400
    
    payment = Payment(**data)
    
    try:
        db.session.add(payment)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating payment."}), 500

    return jsonify(payment.json()), 201

# @app.route("/payment/<int:PaymentID>", methods=['PUT'])
# def update_payment(PaymentID):
#     payment = Payment.query.get(PaymentID)
#     PaymentID = request.json['PaymentID']
#     Password = request.json['Password']

#     customer.CustEmail = CustEmail
#     customer.Password = Password

#     db.session.commit()
#     return payment_schema.jsonify(payment)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5003, debug=True)
