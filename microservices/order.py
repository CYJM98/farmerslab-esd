from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
from textmagic.rest import TextmagicRestClient
import pika
import json
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/orders'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Orders(db.Model):
    __tablename__ = 'orders'
    
    OrderID = db.Column(db.Integer, primary_key=True)
    CustEmail = db.Column(db.String(100), nullable=False)
    ProductName = db.Column(db.String(100), primary_key=True)
    OrderQuantity = db.Column(db.Integer, nullable=False)
    DeliveryID = db.Column(db.Integer, nullable=False)
    OrderDate = db.Column(db.DateTime, nullable=False)

    def __init__(self, OrderID, CustEmail, ProductName, OrderQuantity, DeliveryID, OrderDate):
        self.OrderID = OrderID
        self.CustEmail = CustEmail
        self.ProductName = ProductName
        self.OrderQuantity = OrderQuantity
        self.DeliveryID = DeliveryID
        self.OrderDate = OrderDate

    def json(self):
        return {"OrderID": self.OrderID,
                "CustEmail": self.CustEmail,
                "ProductName": self.ProductName, 
                "OrderQuantity":self.OrderQuantity, 
                "DeliveryID": self.DeliveryID,
                "OrderDate": self.OrderDate
                }


@app.route("/order")
def get_all():
    return jsonify({"orders": [orders.json() for orders in Orders.query.all()]})


@app.route("/order/<int:OrderID>", methods=['GET'])
def find_by_OrderID(OrderID):
    order = {"orders": [orders.json() for orders in Orders.query.filter_by(OrderID=OrderID)]}
    if order:
        return jsonify(order)
    return jsonify({"message": "OrderID not found."}), 404

@app.route("/order", methods=['POST'])
def create_order():
    print("inserted")
    
    data = request.get_json()
    OrderID = data["OrderID"]
    ProductName = data["ProductName"]

    if (Orders.query.filter_by(OrderID=OrderID, ProductName=ProductName).first()):
        return jsonify({"message": "Order'{}' already exists.".format(OrderID)}), 400
    
    order = Orders(**data)
    print(order)
    type(order)
    
    try:
        db.session.add(order)
        db.session.commit()
        send_order(order.json())
        CustEmail = data["CustEmail"]
        phoneNum = "65" + str(getCustomerInfo(CustEmail))
        message = "Dear customer, your order has been confirmed. You can track your order with the following OrderID: " + str(OrderID) + ". Thank you for shopping at The Farmers Lab!"
        #sendSMS(phoneNum, message)
    except:
        return jsonify({"message": "An error occurred creating order."}), 500
    return jsonify(order.json()), 201

def getCustomerInfo(email):
    url = "http://localhost:5000/customer/" + email
    data = requests.get(url)
    json_data = data.json()    
    return json_data["MobileNum"]

def sendSMS(number, message):
    username = "xiaoyenkua"
    token = "WLiObqlZaiLOcGBApVuUinC4xz3KY7"
    client = TextmagicRestClient(username, token)
  
    message = client.messages.create(phones=number, text=message)

def send_order(order):
    hostname = "localhost" # default broker hostname. Web management interface default at http://localhost:15672
    port = 5672 # default messaging port.
    # connect to the broker and set up a communication channel in the connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
    # Note: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
    # If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls
    channel = connection.channel()
    channel.queue_declare(queue='order')

    # prepare the message body content
    message = json.dumps(order, default=str) # convert a JSON object to a string
    print(message)
    # send the message
    # always inform Monitoring for logging no matter if successful or not
    channel.basic_publish(exchange="", routing_key="order", body=message)
    print("Publish to the queue")
    connection.close()

@app.route("/order/<int:OrderID>", methods=['PUT'])
def update_order(OrderID):
    order = Orders.query.get(OrderID)
    OrderID = request.json['OrderID']
    CustEmail = request.json['CustEmail']
    ProductName = request.json['ProductName']
    OrderQuantity = request.json['OrderQuantity']
    DeliveryID = request.json['DeliveryID']
    OrderDate = request.json['OrderDate']

    order.OrderID = OrderID
    order.CustEmail = CustEmail
    order.ProductName = ProductName
    order.OrderQuantity = OrderQuantity
    order.DeliveryID = DeliveryID
    order.OrderDate = OrderDate

    db.session.commit()
    return orders_schema.jsonify(order)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)
