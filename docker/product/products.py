from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/product'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('dbURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

class Product(db.Model):
    __tablename__ = 'product'
    
    ProductName = db.Column(db.String(100), primary_key=True)
    ProductType = db.Column(db.String(100), nullable=False)
    ProductDescription = db.Column(db.String(999), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    UnitPrice = db.Column(db.Float(precision=2), nullable=False)
    UnitWeight = db.Column(db.Float(precision=1), nullable=False)
    ProductImage = db.Column(db.String(50), nullable=False)

    def __init__(self, ProductName, ProductType, ProductDescription, Quantity, UnitPrice, UnitWeight, ProductImage):
        self.ProductName = ProductName
        self.ProductType = ProductType
        self.ProductDescription = ProductDescription
        self.Quantity = Quantity
        self.UnitPrice = UnitPrice
        self.UnitWeight = UnitWeight
        self.ProductImage = ProductImage

    def json(self):
        return {"ProductName": self.ProductName,
                "ProductType": self.ProductType,
                "ProductDescription": self.ProductDescription, 
                "Quantity": self.Quantity,
                "UnitPrice": self.UnitPrice,
                "UnitWeight": self.UnitWeight,
                "ProductImage": self.ProductImage,
                }

@app.route("/product")
def get_all():
    return jsonify({"products": [product.json() for product in Product.query.all()]})


@app.route("/product/<string:ProductName>", methods=['GET'])
def find_by_ProductName(ProductName):
    product = Product.query.filter_by(ProductName=ProductName).first()
    if product:
        return jsonify(product.json())
    return jsonify({"message": "Product not found."}), 404

@app.route("/product", methods=['POST'])
def create_product():
    data = request.get_json()

    ProductName = data["ProductName"]

    if (Product.query.filter_by(ProductName=ProductName).first()):
        return jsonify({"message": "Product '{}' already exists.".format(ProductName)}), 400

    product = Product(**data)

    try:
        db.session.add(product)
        db.session.commit()
    except:
        return jsonify({"message": "An error occurred creating product."}), 500

    return jsonify(product.json()), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

# 1) set dbURL=mysql+mysqlconnector://root@localhost:3306/product
# python products.py
# pip install -r requirements.txt
# 2) docker build -t ycm98/product:1.0.0 .
# View Images: docker images
# Remove Image: docker rmi <image id>
# 3) docker run -p 5001:5001 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/product ycm98/product:1.0.0
# 4) docker run -p 5100:5001 -e dbURL=mysql+mysqlconnector://is213@host.docker.internal:3306/product ycm98/product:1.0.0	
# Container (Start): docker start <containerid> (Stop): docker stop 
# (Check): docker ps (Logs): docker logs (Remove) docker rm <containerid>