from flask import Flask
app = Flask(_name_)

@app.route("/")
def home():
    return "Hello, Flask!"


{"cart_value": 790, "delivery_distance": 2235, "number_of_items": 4, "time": "2024-01-15T13:00:00Z"}
http://127.0.0.1:5000/calculate_delivery_fee