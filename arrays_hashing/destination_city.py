"""
PROBLEM:
- We are given a two dimensional array
- each sub array is composed of two cities
  these two cities have a direct path from sub_arr[0] --> sub_arr[1]
- we need to return the destination city
  destinatin city == city that has no path outgoing to another city
- Basically destination city will be at sub_arr[1] and no sub_arr[0] would be equal to it

EXAMPLES:
Input: [
  ["London","New York"],
  ["New York","Lima"],
  ["Lima","Sao Paulo"]
]
Output: "Sao Paulo" 

Input: [
  ["B","C"],
  ["D","B"],
  ["C","A"]
]
Output: "A"

Input: [["A","Z"]]
Output: "Z"

There will exactly be one destination city
What if paths are empty? Nope it will have atleast one sub array
Can the city names be in different case in different sub arrays?
each path will have 2 cities
  they won't be the same
each city will have at least one character

Approach:
- initialize two variables that are pointing to sets
  departure_cities, arrival_cities
- we will iterate over the main paths array
  on each iteration, add one city to the departure_cities and one to arrival_cities
- at the end we minus departures from arrivals

PSEUDO CODE:
DEF dest_city(paths):
    dep_cities = set()
    arr_cities = set()
    FOR path in paths:
        dep_cities.add(path[0])
        arr_cities.add(path[1])
    RETURN (arr_cities - dep_cities).pop()
"""

def dest_city(paths):
    dep_cities = set()
    arr_cities = set()

    for path in paths:
        dep_cities.add(path[0])
        arr_cities.add(path[1])
    
    return (arr_cities - dep_cities).pop()

print(dest_city([
    ["London","New York"],
    ["New York","Lima"],
    ["Lima","Sao Paulo"]
]))


print(dest_city([
    ["B","C"],
    ["D","B"],
    ["C","A"]
]))