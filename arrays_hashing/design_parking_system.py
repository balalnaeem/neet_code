"""
PROBLEM:
- design a parking system for a parking lot
- parking lot has three kinds of spaces: big, medium and small
- each size has fixed number of slots
- we are to implement the ParkingSystem class
- spaces are given as integers for  big, medium and small spaces in the car park as input for the constructor
- our method add car would check whether there is parking space for the car type
  that is trying to get into the car park
- a car only park into the parking space of it's type
- our method would return true or false depending on whether the space is available
- cars are denoted as 1 2 or 3 meaning big medium and small respectively
1 == big
2 == medium
3 == small

Example:
Input
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
Output
[null, true, true, false, false]

Breakdown:
- we basically have to update the parking spaces each time we add a car to the parking lot
- so the next time when we check, it is checked with the updated info
"""

class ParkingSystem:
    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small
    
    def add_car(self, carType):
        if carType == 1:
          if self.big >= 1:
              self.big -= 1 
              return True
          else:
              return False
        elif carType == 2:
            if self.medium >= 1:
                self.medium -= 1
                return True
            else:
                return False
        else:
            if self.small >= 1:
                self.small -= 1
                return True
            else:
                return False
