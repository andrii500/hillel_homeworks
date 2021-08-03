from create_db import Sales, app

from flask import request


@app.route("/")
def index():
    return f"""<p>Path: /summary/</p>
               <p>Path: /sales/</p>
               <p>Path: /sales/?product=Value1</p>
               <p>Path: /sales/?payment_type=Value2</p>
               <p>Path: /sales/?product=Value1&payment_type=Value2</p>"""


@app.route("/summary/")
def get_summary():
    sales_ = Sales.query.all()
    date = ''

    for i in range(1, 32):
        day_price = 0
        for row in sales_:
            if row.transaction_date.day == i:
                day_price += row.price
        date += f"<p>Transaction_date: 01/{i}/2009, day_price: {day_price}</p>"

    return date


@app.route('/sales/')
def get_sales():
    args = request.args
    dict_param = {}
    date = ''

    for key, value in args.items():
        dict_param[key] = value

    if dict_param:
        sales_ = Sales.query.filter_by(**dict_param).all()
        for row in sales_:
            date += f"<p>{row.id}, {row.transaction_date}, {row.product}, {row.price}, {row.payment_type}</p>"
    else:
        sales_ = Sales.query.all()
        for row in sales_:
            date += f"<p>{row.id}, {row.transaction_date}, {row.product}, {row.price}, {row.payment_type}</p>"

    return date
