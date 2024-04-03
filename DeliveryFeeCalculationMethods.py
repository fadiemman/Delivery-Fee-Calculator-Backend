from datetime import datetime, timezone
import math


SMALL_ORDER_THRESHOLD = 1000
DELIVERY_FREE_CART_VALUE_STARTING_RANGE = 20000
INITIAL_BASE_DISTANCE = 1000
BASE_DISTANCE_CHARGES = 200
ADDITIONAL_HALF_KM_CHARGES = 100
ADDITIONAL_DISTANCE_PATCH = 500
ITEM_THRESHOLD = 4
ABOVE_ITEM_THRESHOLD_SURCHARGE = 50
BULK_ITEM_THRESHOLD = 12
BULK_ITEM_SURCHARGE = 120
MAX_DELIVERY_FEE = 1500
RUSH_HOUR_STARTING_TIME = 15
RUSH_HOUR_END_TIME = 19
FRIDAY_RUSH_MULTIPLYING_FACTOR = 1.2
NO_DELIVERY_CHARGES = 0
CONSTANT_ONE = 1

def calculate_small_order_surcharge(cart_value):
    """
    This function calculates the small order surcharge. If the cart value is below 10 euros, it returns the 
    additional charges to be applied to the overall delivery charges.
    """
    small_order_fee = max(SMALL_ORDER_THRESHOLD - cart_value, 0)
    return small_order_fee

def calculate_distance_charges(delivery_distance):
    """
    This function calculates the delivery charges based on the provided 
    distance and returns the surcharge specific to the distance.
    """
    if (delivery_distance <= INITIAL_BASE_DISTANCE):
        distance_fee = BASE_DISTANCE_CHARGES

    else:
        additional_distance = max(delivery_distance - INITIAL_BASE_DISTANCE, 0)
        additional_distance_divison_result = math.ceil(additional_distance / ADDITIONAL_DISTANCE_PATCH)
        distance_fee = BASE_DISTANCE_CHARGES + (additional_distance_divison_result * ADDITIONAL_HALF_KM_CHARGES)

    return distance_fee

def calculate_items_surcharge(number_of_items):
    """
    This function calculates the surcharge based on the number of items presents in the cart. 
    This function is also adding the bulk order surcharge in the return value. 
    """
    initial_quantity_charges = max(number_of_items - ITEM_THRESHOLD, 0) * ABOVE_ITEM_THRESHOLD_SURCHARGE
    bulk_quantity_charges = max(number_of_items - BULK_ITEM_THRESHOLD, 0) * BULK_ITEM_SURCHARGE
    item_charges = initial_quantity_charges + bulk_quantity_charges
    return item_charges


def total_delivery_charges_with_rush_hours(total_cart_value, total_distance, total_number_of_items, current_time):
    """
    This function calculates total delivery charges by considering the Friday rush hours and all other surcharges
    """
    exact_day_today = current_time.weekday()
    print("Weekday is ",exact_day_today)
    separate_hour_time = current_time.hour
    print("hour time is ", separate_hour_time)
    separate_minute_time = current_time.minute
    print("minute time is ", separate_minute_time)
    separate_second_time = current_time.second
    print("second time is ", separate_second_time)
    total_delivery_surcharge_without_rush_hours = calculate_small_order_surcharge(total_cart_value) + calculate_distance_charges(total_distance) + calculate_items_surcharge(total_number_of_items)
   
    if total_cart_value >= DELIVERY_FREE_CART_VALUE_STARTING_RANGE:
        total_delivery_charges = NO_DELIVERY_CHARGES
    else:
        if exact_day_today == 4:
            if RUSH_HOUR_STARTING_TIME <= separate_hour_time < RUSH_HOUR_END_TIME or (separate_hour_time == RUSH_HOUR_END_TIME and (separate_minute_time < CONSTANT_ONE and separate_second_time < CONSTANT_ONE)):
                total_delivery_charges = min(total_delivery_surcharge_without_rush_hours * FRIDAY_RUSH_MULTIPLYING_FACTOR, MAX_DELIVERY_FEE)
            else:
                total_delivery_charges = min(total_delivery_surcharge_without_rush_hours, MAX_DELIVERY_FEE)
        else:
            total_delivery_charges = min(total_delivery_surcharge_without_rush_hours, MAX_DELIVERY_FEE)
    return total_delivery_charges