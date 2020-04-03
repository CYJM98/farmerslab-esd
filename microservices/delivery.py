from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
# import pika
# import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/delivery'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Delivery(db.Model):
    __tablename__ = 'delivery'
    
    DeliveryID = db.Column(db.Integer, primary_key=True)
    OrderID = db.Column(db.Integer, nullable=False)
    OrderTrackingID = db.Column(db.String(100), nullable=False)
    DeliveryDate = db.Column(db.String(100), nullable=False)
    DeliveryStatus = db.Column(db.Integer, nullable=False)

    def __init__(self, DeliveryID, OrderID, OrderTrackingID, DeliveryDate, DeliveryStatus):
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
    return jsonify({"delivery": [delivery.json() for delivery in Delivery.query.all()]})

@app.route("/delivery/<int:DeliveryID>", methods=['GET'])
def find_by_DeliveryID(DeliveryID):
    delivery = Delivery.query.filter_by(DeliveryID=DeliveryID).first()
    if delivery:
        return jsonify(delivery.json())
    return jsonify({"message": "DeliveryID not found."}), 404

@app.route("/delivery/<int:DeliveryID>", methods=['PUT'])
def update_deliverydate(DeliveryID):
    delivery = Delivery.query.get(DeliveryID)

    OrderTrackingID = request.json['OrderTrackingID']
    DeliveryDate = request.json['DeliveryDate']
    DeliveryStatus = request.json['DeliveryStatus']
    
    delivery.OrderTrackingID = OrderTrackingID
    delivery.DeliveryDate = DeliveryDate
    delivery.DeliveryStatus = DeliveryStatus

    db.session.commit()
    return delivery_schema.jsonify(delivery)

# def createDelivery():
#     connection = pika.BlockingConnection(
#         pika.ConnectionParameters(host='localhost'))
#     channel = connection.channel()

#     channel.queue_declare(queue='order')

#     def callback(ch, method, properties, body):
#         print(" [x] Received %r" % body)
        
#         data = json.loads(body) # Convert string into json
#         print(data)
#         delivery = Delivery(DeliveryID=data["DeliveryID"], OrderID=data["OrderID"], OrderTrackingID="", DeliveryDate="", DeliveryStatus=0) 
#         try:
#             db.session.add(delivery)
#             db.session.commit()
#         except:
#             print("Error in adding to database")

#         ##item = json.loads(body)
#     channel.basic_consume(
#         queue='order', on_message_callback=callback, auto_ack=True)

#     channel.start_consuming()
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5004, debug=True)
