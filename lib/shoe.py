#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, condition = "New"):
        self.size = size
        self.brand = brand
        self.repaired_shoe = True
        self.condition = condition

    def repair(self):
        self.condition
    
    def cobble(self):
        self.repaired_shoe = True
        print('Your shoe is as good as new!')
        
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print('size must be an integer')
        else:
            self._size = value
