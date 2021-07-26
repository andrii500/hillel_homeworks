import csv
from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sales.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Sales(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_date = db.Column(db.DateTime, unique=False, nullable=False)
    product = db.Column(db.String(80), unique=False, nullable=False)
    price = db.Column(db.Integer, unique=False, nullable=False)
    payment_type = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return '<Transaction_date %r>' % self.transaction_date


def main():
    db.create_all()
    with open('hw.csv', encoding='utf-8') as read_files:
        data = csv.DictReader(read_files, delimiter=";")
        for row in data:
            sales = Sales(transaction_date=datetime.strptime(row['Transaction_date'], '%m/%d/%Y %H:%M'),
                          product=row['Product'], price=int(row['Price']), payment_type=row['Payment_Type'])
            db.session.add(sales)
        db.session.commit()


if __name__ == '__main__':
    main()
