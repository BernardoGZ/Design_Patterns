import csv
from patterns import ride as ride_class
from datetime import datetime

'''
    SOLID Principles applied:
        - SRP: csv_utils should only be responsible for CSV management
        - OCP: In case any other CSV functionalities added, can be added without
        modifying old code
'''

def parse_file(csv_file: str):
    with open(csv_file) as file:
        csv_reader = csv.DictReader(file, delimiter=",")
        rides = []
        for row in csv_reader:
            ride = (ride_class.RideBuilder()
            .with_error("")
            .with_taxi_id(row['TaxiID'])
            .with_pick_up_time(datetime.strptime(row['lpep_pickup_datetime'], '%Y-%m-%d %H:%M:%S'))
            .with_drop_of_time(datetime.strptime(row['lpep_dropoff_datetime'], '%Y-%m-%d %H:%M:%S'))
            .with_passenger_count(int(row["passenger_count"]))
            .with_trip_distance(float(row["trip_distance"]))
            .with_tolls_amount(float(row["total_amount"]))            
            )

            rides.append(ride)
        return rides


