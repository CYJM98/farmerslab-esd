from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
import pika


# hostname = "localhost" # default hostname
# port = 5672 # default port
# # connect to the broker and set up a communication channel in the connection
# connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
#     # Note: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
#     # If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls
# channel = connection.channel()
# # set up the exchange if the exchange doesn't exist
# exchangename="order_fanout"
# channel.exchange_declare(exchange=exchangename, exchange_type='fanout')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/delivery'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Delivery(db.Model):
    __tablename__ = 'delivery'
    
    DeliveryID = db.Column(db.Integer, primary_key=True)
    OrderID = db.Column(db.Integer, nullable=False)
    OrderTrackingID = db.Column(db.Integer, nullable=False)
    DeliveryDate = db.Column(db.DateTime, nullable=False)
    DeliveryStatus = db.Column(db.Integer, nullable=False)

    def __init__(self, DeliveryID, OrderID, OrderTrackingID, DeliveryDate):
        self.DeliveryID = DeliveryID
        self.OrderID = OrderID
        self.OrderTrackingID = OrderTrackingID
        self.DeliveryDate = DeliveryDate
        self.DeliveryStatus = DeliveryStatus
        
    def json(self):
        return {"DeliveryID": self.DeliveryID,
                "OrderID": self.OrderID,
                "OrderTrackingID": self.OrderTrackingID, 
                "DeliveryDate": self.DeliveryDate, 
                "DeliveryStatus": self.DeliveryStatus
                }       

@app.route("/delivery")
def get_all():
    return jsonify({"deliveries": [delivery.json() for delivery in Delivery.query.all()]})


@app.route("/delivery/<int:DeliveryID>", methods=['GET'])
def find_by_DeliveryID(DeliveryID):
    delivery = Delivery.query.filter_by(DeliveryID=DeliveryID).first()
    if delivery:
        return jsonify(delivery.json())
    return jsonify({"message": "DeliveryID not found."}), 404

@app.route("/delivery", methods=['POST'])
def create_delivery():
    data = request.get_json()
    DeliveryID = data["DeliveryID"]

    if (Delivery.query.filter_by(DeliveryID=DeliveryID).first()):
        return jsonify({"message": "Delivery with an ID'{}' already exists.".format(DeliveryID)}), 400
    
    delivery = Delivery(**data)
    
    try:
        db.session.add(delivery)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating delivery."}), 500

    return jsonify(delivery.json()), 201

@app.route("/delivery/<int:DeliveryID>", methods=['PUT'])
def update_deliverydate(DeliveryID):
    delivery = Delivery.query.get(DeliveryID)
    DeliveryID = request.json['DeliveryID']
    OrderID = request.json['OrderID']
    OrderTrackingID = request.json['OrderTrackingID']
    DeliveryDate = request.json['DeliveryDate']
    DeliveryStatus = request.json['DeliveryStatus']

    delivery.DeliveryID = DeliveryID
    delivery.DeliveryDate = DeliveryDate
    delivery.DeliveryStatus = DeliveryStatus

    db.session.commit()
    return delivery_schema.jsonify(delivery)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5004, debug=True)
