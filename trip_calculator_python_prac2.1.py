# Trip Cost and Distance Calculator
# This program calculates total distance, average distance, fuel required, fuel cost, and average speed based on user input.

#users enters a distance for each trip
distance_1 = input("Enter the distance of trip #1 (in kilometers): ")
distance_2 = input("Enter the distance of trip #2 (in kilometers): ")

concatenated_distances = distance_1 + distance_2

#print the strings distance value added
print(f"\nConcatenated distances: {concatenated_distances}")

#users enters a distance for each trip, again
distance_1 = float(distance_1)
distance_2 = float(distance_2)

total_distance_travelled = distance_1 + distance_2
average_distance = total_distance_travelled / 2

#print the total and average of the trip
print(f"\nTotal distance travelled: {total_distance_travelled:.1f} km")
print(f"Average distance travelled: {average_distance:.1f} km")

#user enter the fuel price and vehicle consumption 
fuel_price = float(input("\nEnter the fuel price per litre: "))
vehicle_fuel_consumption = float(input("Enter the vehicle’s fuel consumption (in kilometers per litre): "))

total_fuel_required = total_distance_travelled / vehicle_fuel_consumption
total_cost_of_fuel = fuel_price * total_fuel_required

print(f"\nThe total amount of the fuel required: {total_fuel_required:.1f} L")
print(f"The total cost of the fuel: R {total_cost_of_fuel:.1f}")

#users inputs the time taken in the trip to calc to avgerage speed of the trip 
total_time = float(input("\nEnter the total time the trip took (in hours): "))
average_speed = total_distance_travelled / total_time

print(f"\nAverage speed of the trip: {average_speed:.1f} km/h")
