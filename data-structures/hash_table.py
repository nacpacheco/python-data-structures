from random import randint

class HashTable():

    def __init__(self, length = 4):
        self.hash_table = [None] * length

    def hash(self, key):
        return hash(key) % len(self.hash_table)
    
    def add(self, key, value):
        hash_key = self.hash(key)
        if self.hash_table[hash_key] is not None:
            for kvp in self.hash_table[hash_key]:
                if kvp[0] == key:
                    kvp[1] = value
                break
            else:
                self.hash_table[hash_key].append([key,value])
        else:
            self.hash_table[hash_key] = []
            self.hash_table[hash_key].append([key,value])

        if self.is_full():
            self.double()

    def get(self,key):
        hash_key = self.hash(key)
        if self.hash_table[hash_key] is None:
            raise KeyError()
        else:
            for kvp in self.hash_table[hash_key]:
                if kvp[0] == key:
                    return kvp[1]
            raise KeyError()

    def is_full(self):
        items = 0
        for item in self.hash_table:
            if item is not None:
                items += 1
        return items > len(self.hash_table)/2

    def double(self):
        ht2 = HashTable(length=len(self.hash_table)*2)
        for i in range(len(self.hash_table)):
            if self.hash_table[i] is None:
                continue

            for key, value in self.hash_table[i]:
                ht2.add(key, value)

        self.hash_table = ht2

    def __setitem__(self, key, value):
        self.add(key, value)
    
    def __getitem__(self,key):
        return self.get(key)

    def __str__(self):
        return str(self.__dict__)

hashtable = HashTable(5)
import pdb; pdb.set_trace()