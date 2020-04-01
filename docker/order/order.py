from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/orders'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
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
    
    try:
        db.session.add(order)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating order."}), 500

    return jsonify(order.json()), 201

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
    app.run(host='0.0.0.0', port=5002, debug=True)

# 1) set dbURL=mysql+mysqlconnector://root@localhost:3306/orders
# python order.py
# pip install -r requirements.txt
# 2) docker build -t ycm98/order:1.0.0 .
# View Images: docker images
# Remove Image: docker rmi <image id>
# 3) docker run -p 5000:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/order ycm98/order:1.0.0
# 4) docker run -p 5900:5000 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/order ycm98/order:1.0.0	
# Container (Start): docker start <containerid> (Stop): docker stop 
# (Check): docker ps (Logs): docker logs (Remove) docker rm <containerid>
