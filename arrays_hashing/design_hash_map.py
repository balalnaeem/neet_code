"""
PROBLEM:-
- impplement a hash map class
- MyHashMap() initializes object with an empty array

- put inserts a key value pair inside the hash map
  if the key already exists, just update the value


"""

class MyHashMap:

    def __init__(self):
      self.hash_map = []

    def put(self, key, value):
        for pair in self.hash_map:
            if pair[0] == key:
                pair[1] = value
                return

        self.hash_map.append([key, value])

    def get(self, key):
        for pair in self.hash_map:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        for idx in range(len(self.hash_map)):
            if self.hash_map[idx][0] == key:
                del self.hash_map[idx]
                return
                

myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
print(myHashMap.get(1))
print(myHashMap.get(3))
myHashMap.put(2, 1)
print(myHashMap.get(2))
myHashMap.remove(2)

print(myHashMap.hash_map)