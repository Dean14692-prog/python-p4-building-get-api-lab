from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return "<h1>Bakery GET API</h1>"

# GET /bakeries: Return all bakeries
@app.route('/bakeries', methods=['GET'])
def get_bakeries():
    bakeries = Bakery.query.all()
    bakery_list = [bakery.to_dict(rules=['-baked_goods.bakery']) for bakery in bakeries]
    return jsonify(bakery_list), 200

# GET /bakeries/<int:id>: Return one bakery with its baked goods
@app.route('/bakeries/<int:id>', methods=['GET'])
def get_bakery_by_id(id):
    bakery = Bakery.query.get_or_404(id)
    return jsonify(bakery.to_dict(rules=['baked_goods'])), 200

# GET /baked_goods/by_price: Return baked goods sorted by price (desc)
@app.route('/baked_goods/by_price', methods=['GET'])
def baked_goods_by_price():
    goods = BakedGood.query.order_by(BakedGood.price.desc()).all()
    goods_list = [good.to_dict(rules=['bakery']) for good in goods]
    return jsonify(goods_list), 200

# GET /baked_goods/most_expensive: Return the most expensive baked good
@app.route('/baked_goods/most_expensive', methods=['GET'])
def most_expensive_baked_good():
    most_expensive = BakedGood.query.order_by(BakedGood.price.desc()).first()
    return jsonify(most_expensive.to_dict(rules=['bakery'])), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)
