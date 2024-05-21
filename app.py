from flask import Flask, render_template, jsonify, request
import sqlite3
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Function to connect to the SQLite database
def connect_db():
    conn = sqlite3.connect('stocks.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:stock_id>', methods=['GET'])
def get_byStock(stock_id):
    conn = connect_db()
    cursor = conn.cursor()
    # Query the database to get the price of the stock for all dates
    cursor.execute("SELECT Price FROM stockP WHERE Stock = ?", (stock_id,))
    rows = cursor.fetchall()
    rows = [row[0] for row in rows]
    print(rows)
    conn.close()

    return jsonify(rows)


@app.route('/<string:stock_id>/<string:date>', methods=['GET'])
def get_byStockDate(stock_id, date):
    logging.info(stock_id)
    logging.info(date)
    logging.info('pass')
    conn = connect_db()
    cursor = conn.cursor()
    # Query the database to get the price of the stock for all dates
    cursor.execute("SELECT Price FROM stockP WHERE Stock = ? AND Date = ?", (stock_id,date))
    rows = cursor.fetchall()
    rows = [row[0] for row in rows]
    print(rows)
    conn.close()

    return jsonify(rows)


@app.route('/test', methods=['GET'])
def handle_post():
    data = request.json
    stock_id = data['stock_id']
    date = data['date']

    # Do something with the received data
    print(f"Received POST request with stock_id: {stock_id}, date: {date}")

    # Return a response if needed
    return "Success"

if __name__ == '__main__':
    app.run(debug=True)
