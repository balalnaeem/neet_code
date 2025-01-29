"""
PROBLEM:
- implement MyHashSet class
- add(key) inserts the key into the HashSet and returns None
- contains(key) returns bool depending on whether or not key exists in the HashSet
- remove(key) remomves the value key from the HashSet and do nothing if the key doesn't exist

initialize:
  - just set the set equal to an empty array
add:
  - so for adding, since the set can't hold duplicates, all vals are unique
  - we would first check whether the value already exists in the set, if it does
    we won't add it. Do nothing
  - if it doesn't we will add it, return nothing
contains:
  - so for contains, we need to just check whether a key exists in the hash set
  - we can do that with in operator

"""

class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key):
        if key not in self.set:
            self.set.append(key)
        
        

    def remove(self, key):
        if key in self.set:
            self.set.remove(key)
        

    def contains(self, key):
        return True if key in self.set else False


myHashSet = MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
print(myHashSet.contains(1))
print(myHashSet.contains(3))
myHashSet.add(2)      
myHashSet.contains(2)
myHashSet.remove(2)
myHashSet.contains(2)

print(myHashSet.set)