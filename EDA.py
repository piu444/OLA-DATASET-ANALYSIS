import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv('ola_dataset_cleaned.csv')

# ride volume over time
# df['Date'] = pd.to_datetime(df['Date'])
# df['Only_Date'] = df['Date'].dt.date
# rides_over_time = df.groupby('Only_Date').size()
# plt.figure(figsize=(12, 5))
# rides_over_time.plot()
# plt.title("Ride Volume Over Time (Daily)")
# plt.xlabel("Date")
# plt.ylabel("Number of Rides")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# booking status distribution
# df['Booking_Status'].value_counts().plot(kind='bar')
# plt.title("Booking Status Breakdown")
# plt.xlabel("Status")
# plt.ylabel("Count")
# plt.show()

# Top 5 Vehicle Types by Ride Distance
# vehicle_distance = df.groupby('Vehicle_Type')['Ride_Distance'].sum().sort_values(ascending=False)
# vehicle_distance.head().plot(kind='bar')
# plt.title("Top 5 Vehicle Types by Ride Distance")
# plt.xlabel("Vehicle Type")
# plt.ylabel("Total Ride Distance")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
# plt.savefig('vehicle_type_ride_distance.png')


# Average Customer Ratings by Vehicle Type
# avg_ratings = df.groupby('Vehicle_Type')['Customer_Rating'].mean().sort_values(ascending=False)
# avg_ratings.plot(kind='bar')
# plt.title("Average Customer Ratings by Vehicle Type")
# plt.xlabel("Vehicle Type")
# plt.ylabel("Average Rating")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
# plt.savefig('vehicle_type_avg_ratings.png')

# Cancellation Reasons Analysis


# # Revenue by Payment Method
# df.groupby('Payment_Method')['Booking_Value'].sum().plot(kind='bar')
# plt.title("Revenue by Payment Method")
# plt.xlabel("Payment Method")
# plt.ylabel("Revenue")
# plt.show()

# # Driver Ratings Distribution
# plt.hist(df['Driver_Ratings'], bins=10)
# plt.title("Driver Ratings Distribution")
# plt.xlabel("Rating")
# plt.ylabel("Frequency")
# plt.show()
# plt.savefig('driver_ratings_distribution.jpg')

# Customer vs Driver Ratings
summary = df.groupby('Customer_Rating')['Driver_Ratings'].mean()

plt.figure(figsize=(8,5))
summary.plot(marker='o')
plt.title("Average Driver Rating by Customer Rating")
plt.xlabel("Customer Rating")
plt.ylabel("Average Driver Rating")
plt.grid(True)
plt.tight_layout()
plt.show()

