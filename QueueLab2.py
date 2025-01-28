# Listing 4-5
# Implement a Queue data structure using a Python list

# Changed naming to use under_scores instead of mixedCase
# member name __queue instead of __que 
# removed inheritance from object since not needed in Python 3
# using RuntimeError instead of base Exception for overflow/ underflow

# ------------------------
# ADDED: 2025-01-28, Josefina
# Class Deque with functions insert_left, insert_right, remove_left, remove_right
# ------------------------
class Deque:
    def __init__(self, size):
        self.__max_size = size              # size of circular array
        self.__deque = [None]*size          # deque stored as list
        self.__front = 0                    # empty deque has front 0
        self.__rear = -1                    # empty deque has rear -1
        self.__n_items = 0                  # number of items in deque

    def is_empty(self):
        return self.__n_items == 0
    
    def is_full(self):
        return self.__n_items == self.__max_size
    
    def __str__(self):
        content = []
        front = self.__front
        for __ in range(self.__n_items):
            content.append(self.__deque[front])
            front = (front + 1) % self.__max_size
        return f"{content}, front={self.__front}, rear={self.__rear}, size={self.__n_items}"
    
    def insert_left(self, item):
        if self.is_full():
            raise RuntimeError("Deque overflow") # raise exception if deque is full
        
        # move front one step to the left
        self.__front = (self.__front - 1) % self.__max_size
        self.__deque[self.__front] = item # insert item at new front
        self.__n_items += 1 # increase number of items

    def insert_right(self, item):
        if self.is_full():
            raise RuntimeError("Deque overflow") # raise exception if deque is full
        
        # move rear one step to the right
        self.__rear = (self.__rear + 1) % self.__max_size
        self.__deque[self.__rear] = item # insert item at new rear
        self.__n_items += 1 # increase number of items

    def remove_left(self):
        if self.is_empty():
            raise RuntimeError("Deque underflow") # raise exception if deque is empty
        
        front = self.__deque[self.__front] # get item at front
        self.__deque[self.__front] = None # remove item at front (not necessary but used for clarity and debugging)
        self.__front = (self.__front + 1) % self.__max_size # move front one step to the right
        self.__n_items -= 1 # decrease number of items
        return front # return item at front

    def remove_right(self):
        if self.is_empty():
            raise RuntimeError("Deque underflow") # raise exception if deque is empty
        
        rear = self.__deque[self.__rear] # get item at rear
        self.__deque[self.__rear] = None # remove item at rear (not necessary but used for clarity and debugging)
        self.__rear = (self.__rear - 1) % self.__max_size # move rear one step to the left
        self.__n_items -= 1 # decrease number of items
        return rear # return item at rear

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
    

if __name__ == "__main__":
    # Create a Deque with a size of 5
    deque = Deque(5)

    # Insert elements at the right
    print("Inserting elements at the right:")
    deque.insert_right(10)
    deque.insert_right(20)
    deque.insert_right(30)
    print(deque) # [10, 20, 30, None, None], front=0, rear=2, size=3

    # Insert elements at the left
    print("\nInserting elements at the left:")
    deque.insert_left(5)
    print(deque) # [10, 20, 30, None, 5], front=4, rear=2, size=4

    # Remove elements from the left
    print("\nRemoving elements from the left:")
    removed = deque.remove_left()
    print(f"Removed: {removed}") # Removed: 5
    print(deque) # [10, 20, 30, None, None], front=0, rear=2, size=3

    # Remove elements from the right
    print("\nRemoving elements from the right:")
    removed = deque.remove_right()
    print(f"Removed: {removed}") # Removed: 30
    print(deque) # [10, 20, None, None, None], front=0, rear=1, size=2

    # Trying to add more elements than the size of the deque
    print("\nTrying to add more elements than the size of the deque:")
    deque.insert_right(40)
    deque.insert_right(50)
    deque.insert_right(60)
    print(deque) # [10, 20, 40, 50, None], front=0, rear=4, size=4

    try:
        deque.insert_right(70)
    except RuntimeError as e:
        print(f"Error: {e}") # Error: Deque overflow
    
    # Trying to remove elements from an empty deque
    print("\nTrying to remove elements from an empty deque:")
    deque.remove_left()
    deque.remove_left()
    deque.remove_left()
    deque.remove_left()
    deque.remove_left()
    print(deque) # [None, None, None, None, None], front=0, rear=4, size=0

    try:
        deque.remove_left()
    except RuntimeError as e:
        print(f"Error: {e}") # Error: Deque underflow