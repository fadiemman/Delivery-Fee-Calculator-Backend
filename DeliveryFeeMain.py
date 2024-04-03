from flask import Flask, request, jsonify
import json
# import requests
from datetime import datetime
from DeliveryFeeCalculationMethods import total_delivery_charges_with_rush_hours


app = Flask(__name__)

@app.route('/calculate_delivery_fee', methods=['POST'])
def calculate_delivery_fee():
    """
    This function extract the information from the POST payload, 
    calculate the total total deliery charges and return JSON response 
    containing calculated charges. 
    """
    try:
        input_data = request.get_json()

        #print("Inpit data",input_data)

        total_cart_value = input_data["cart_value"]
        total_delivery_distance = input_data["delivery_distance"]
        total_number_of_items = input_data["number_of_items"]
        time_string = input_data["time"]

        # Validate non-negative input values
        if any(value < 0 for value in [total_cart_value, total_delivery_distance, total_number_of_items]):
            return jsonify({"Invalid input values. Please provide non-negative values for cart_value, delivery_distance and number_of_items"})

        # Validate time format
        try:
            # Converting this time string into dateTime object
            utc_time = datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            return jsonify({"Invalid time format. Please provide the field in 'YYYY-MM-DDTHH:MM:SSZ'."})

        # Calculating overall delivery charges
        Overall_delivery_charges = total_delivery_charges_with_rush_hours(total_cart_value, total_delivery_distance, total_number_of_items, utc_time)

        # Create response payload
        output_data = {"delivery_dee" : Overall_delivery_charges}

        return jsonify(output_data)
    
    except json.JSONDecodeError as e:
        print("Error decofing   JSON : ", e)
    except ValueError as e:
        print(f"Error converting time_string to datetime : {e}")
    except Exception as e:
        print(f"Unexpected error occure : {e}")



if __name__=="__main__":
    app.run(debug=True)