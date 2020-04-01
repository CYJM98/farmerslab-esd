from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
#import pika

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/order'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Order(db.Model):
    __tablename__ = 'order'
    
    OrderID = db.Column(db.Integer, primary_key=True)
    CustEmail = db.Column(db.String(100), nullable=False)
    ProductName = db.Column(db.String(100), nullable=False)
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
    return jsonify({"order": [order.json() for order in Order.query.all()]})


@app.route("/order/<int:OrderID>", methods=['GET'])
def find_by_OrderID(OrderID):
    order = Order.query.filter_by(OrderID=OrderID).first()
    if order:
        return jsonify(order.json())
    return jsonify({"message": "OrderID not found."}), 404

@app.route("/order", methods=['POST'])
def create_order():
    
    data = request.get_json()
    OrderID = data["OrderID"]

    if (Order.query.filter_by(OrderID=OrderID).first()):
        return jsonify({"message": "Order'{}' already exists.".format(OrderID)}), 400
    
    order = Order(**data)
    
    try:
        db.session.add(order)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating order."}), 500

    return jsonify(order.json()), 201

# def send_order(order):
#     # default username / password to the borker are both 'guest'
#     hostname = "localhost" # default broker hostname. Web management interface default at http://localhost:15672
#     port = 5672 # default messaging port.
#     # connect to the broker and set up a communication channel in the connection
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname, port=port))
#         # Note: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
#         # If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls
#     channel = connection.channel()

#     # set up the exchange if the exchange doesn't exist
#     exchangename="order_fanout"
#     channel.exchange_declare(exchange=exchangename, exchange_type='fanout')

#     # prepare the message body content
#     message = json.dumps(order, default=str) # convert a JSON object to a string

#     # send the message
#     # always inform Monitoring for logging no matter if successful or not
#     channel.basic_publish(exchange=exchangename, routing_key="", body=message)
#         # By default, the message is "transient" within the broker;
#         #  i.e., if the monitoring is offline or the broker cannot match the routing key for the message, the message is lost.
#         # If need durability of a message, need to declare the queue in the sender (see sample code below).

#      # prepare the channel and send a message to Shipping
#         channel.queue_declare(queue='shipping', durable=True) # make sure the queue used by Shipping exist and durable
#         channel.queue_bind(exchange=exchangename, queue='shipping') # make sure the queue is bound to the exchange
#         channel.basic_publish(exchange=exchangename, routing_key="", body=message,
#             properties=pika.BasicProperties(delivery_mode = 2, # make message persistent within the matching queues until it is received by some receiver (the matching queues have to exist and be durable and bound to the exchange, which are ensured by the previous two api calls)
#             )
#         )
#         print("Order sent to shipping.")
#     # close the connection to the broker
#     connection.close()

@app.route("/order/<int:OrderID>", methods=['PUT'])
def update_order(OrderID):
    order = Order.query.get(OrderID)
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
    return order_schema.jsonify(order)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)
