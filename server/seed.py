from app import app
from models import db, Bakery, BakedGood

with app.app_context():
    db.drop_all()
    db.create_all()

    bakery1 = Bakery(name="Delightful donuts")
    bakery2 = Bakery(name="Incredible crullers")

    db.session.add_all([bakery1, bakery2])
    db.session.commit()

    goods = [
        BakedGood(name="Chocolate dipped donut", price=2.75, bakery_id=bakery1.id),
        BakedGood(name="Apple-spice filled donut", price=3.5, bakery_id=bakery1.id),
        BakedGood(name="Glazed honey cruller", price=3.25, bakery_id=bakery2.id),
        BakedGood(name="Chocolate cruller", price=100.0, bakery_id=bakery2.id),
    ]

    db.session.add_all(goods)
    db.session.commit()
