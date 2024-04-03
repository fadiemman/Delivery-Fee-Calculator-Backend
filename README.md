# Delivery-Fee-Calculator-Backend

This Delivery Fee Calculator is designed to calculate the delivery charges based on various factors such as cart value, delivery distance, number of items, and time. The calculation takes into account different surcharges, including small order surcharge, distance-based surcharge, and rush hour surcharge.

## Classes and Functions

### DeliveryFeeCalculationMethods 
This class serves as the core module for computing specific surcharges in the delivery fee calculation system. It encapsulates key functions, including calculate_small_order_surcharge, which assesses a surcharge for small orders if the cart  value is below a set threshold, calculate_distance_charges for determining distance-based delivery charges, and calculate_items_surcharge, which calculates surcharges based on the number of items in the cart, including bulk order surcharges. The class also houses total_delivery_charges_with_rush_hours, a function that computes the overall delivery charges, factoring in rush hours, small order surcharge, distance-based surcharge, and additional surcharges.

### DeliveryFeeMain

#### Function: `calculate_delivery_fee()`
This function serves as the main endpoint for calculating delivery fees. It extracts information from the POST payload, validates input values, and calculates the total delivery charges. The response is then returned in JSON format.

To execute the application, initiate the execution of the DeliveryFeeMain class. This class orchestrates the entire delivery fee calculation process, integrating the necessary functions and dependencies.
