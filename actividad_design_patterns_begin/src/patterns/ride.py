# Class: Ride
# Description: Sets the Ride class and its attributes. 
# Uses Builder Design Pattern to instanciate Ride objects

'''
    SOLID Principles applied:
        - SRP: Ride should only be responsible for Ride instances and methods
        - ISP: Ride dataclass used to depend in CSV functionalities. 
        With the refactorization, is not needed anymore
'''

from dataclasses import dataclass
from datetime import datetime

class Ride:
    def __init__(self, error, taxi_id, pick_up_time, drop_of_time, passenger_count, trip_distance, tolls_amount):
        self.error = error
        self.taxi_id = taxi_id
        self.pick_up_time = pick_up_time
        self.drop_of_time = drop_of_time
        self.passenger_count = passenger_count
        self.trip_distance = trip_distance
        self.tolls_amount = tolls_amount

class RideBuilder: 
    def __init__(self):
        self.error = None
        self.taxi_id = None
        self.pick_up_time = None
        self.drop_of_time = None
        self.passenger_count = None
        self.trip_distance = None
        self.tolls_amount = None

    '''
    Setters
    '''

    def with_error(self, error):
        self.error = error
        return self

    def with_taxi_id(self, taxi_id):
        self.taxi_id = taxi_id 
        return self

    def with_pick_up_time (self, pick_up_time):
        self.pick_up_time = pick_up_time 
        return self

    def with_drop_of_time(self, drop_of_time): 
        self.drop_of_time = drop_of_time
        return self
    
    def with_passenger_count(self, passenger_count):
        self.passenger_count = passenger_count 
        return self

    def with_trip_distance (self, trip_distance):
        self.trip_distance = trip_distance 
        return self

    def with_tolls_amount(self, tolls_amount): 
        self.tolls_amount = tolls_amount
        return self

    '''
    Builder
    '''

    def build(self):
        self.product = Ride(
            self.error, 
            self.taxi_id, 
            self.pick_up_time, 
            self.drop_of_time, 
            self.passenger_count, 
            self.trip_distance, 
            self.tolls_amount)
        return self.product

    
    
    
    
    
    
    