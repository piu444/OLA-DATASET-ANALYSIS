# 1. Total rides
TOTAL_RIDES = """
SELECT COUNT(*) AS total_rides
FROM ola_dataset_cleaned;
"""

# 2. Top 5 customers by booking value
TOP_5_CUSTOMERS = """
SELECT Vehicle_Type, SUM(Payment_Method) AS total_value
FROM ola_dataset_cleaned
GROUP BY Vehicle_Type
ORDER BY total_value DESC
LIMIT 5;
"""

# 3. Average customer rating by vehicle type
AVG_RATING_BY_VEHICLE = """
SELECT Vehicle_Type, AVG(Customer_Rating) AS avg_rating
FROM ola_dataset_cleaned
GROUP BY Vehicle_Type;
"""

