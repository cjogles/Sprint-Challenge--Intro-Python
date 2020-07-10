# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle: # BASE CLASS FOR ALL
    pass

class FlightVehicle(Vehicle): # Parent class for starship and airplane classes
    pass

class Starship(FlightVehicle):
    pass

class Airplane(FlightVehicle):
    pass

class GroundVehicle(Vehicle): # Parent class for car and motorcycle classes
    pass

class Car(GroundVehicle):
    pass 

class Motorcycle(GroundVehicle):
    pass