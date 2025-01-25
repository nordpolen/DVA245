# Listing 4-5
# Implement a Queue data structure using a Python list

# Changed naming to use under_scores instead of mixedCase
# member name __queue instead of __que 
# removed inheritance from object since not needed in Python 3
# using RuntimeError instead of base Exception for overflow/ underflow

class Queue:
    def __init__(self, size):
        self.__max_size = size              # size of circular array
        self.__queue = [None]*size          # queue stored as list
        self.__front = 1                    # empty queue has front 1 + rear
        self.__rear = 0                     
        self.__n_items = 0

    def insert(self, item):
        if self.is_full():
            raise RuntimeError("Queue overflow")
        self.__rear = self.__rear + 1 
        if self.__rear == self.__max_size:
            self.__rear = 0
        self.__queue[self.__rear] = item
        self.__n_items += 1
        return True
    
    def remove(self):
        if self.is_empty():
            raise RuntimeError("Queue underflow")
        front = self.__queue[self.__front]
        self.__queue[self.__front] = None
        self.__front = self.__front + 1 
        if self.__front == self.__max_size:
            self.__front = 0
        self.__n_items -= 1
        return front

    def peek(self):
        if self.is_empty():
            return None
        return self.__queue[self.__front]

    def is_empty(self):
        return self.__n_items == 0
    
    def is_full(self):
        return self.__n_items == self.__max_size
    
    def __len__(self):
        return self.__n_items
    
    def __str__(self):
        ans = "["
        j = self.__front
        for i in range(self.__n_items):
            if len(ans) > 1:
                ans += ", "
            ans += self.__queue[j]
            j = (j+1) % self.__max_size
        ans += "]"
        return ans