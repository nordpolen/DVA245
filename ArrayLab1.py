# Implement an Array data structure as a simplified type of list.
# The array should be able to store integers and have the following methods:

class Array(object):
    def __init__(self, initialSize):    # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0                # No items in array initially

    def __len__(self):                  # Special def for len() func
        return self.__nItems             # Return number of items
   
    def get(self, n):                   # Return the value at index n
        if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
            return self.__a[n]            # only return item if in bounds
   
    def set(self, n, value):            # Set the value at index n
        if 0 <= n and n < self.__nItems: # Check if n is in bounds, and
            self.__a[n] = value           # only set item if in bounds
      
    def insert(self, item):             # Insert item at end
        self.__a[self.__nItems] = item   # Item goes at current end
        self.__nItems += 1               # Increment number of items

    def find(self, item):               # Find index for item
        for j in range(self.__nItems):   # Among current items
            if self.__a[j] == item:       # If found,
                return j                   # then return index to item
        return -1                        # Not found -> return -1
   
    def search(self, item):             # Search for item
        return self.get(self.find(item)) # and return item if found

    def delete(self, item):             # Delete first occurrence
        for j in range(self.__nItems):   # of an item
            if self.__a[j] == item:       # Found item
                self.__nItems -= 1         # One fewer at end
                for k in range(j, self.__nItems):  # Move items from
                    self.__a[k] = self.__a[k+1]     # right over 1
                return True                # Return success flag
      
        return False     # Made it here, so couldn't find the item   

    def traverse(self, function=print): # Traverse all items
        for j in range(self.__nItems):   # and apply a function
            function(self.__a[j])

    # ------------------------
    # ADDED: 2025-01-25, Josefina
    # Method to insert an element at a specific position in the array, and a main function to test it
    # ------------------------
    def insert_at(self, position, item):
        # Check if the position is valid
        if position < 0 or position > self.__nItems:
            raise IndexError(f"Position ({position}) if out of range")
        
        # Move elements one step up, starting from the end, borrowing logic from the 'delete' method 
        for i in range(self.__nItems, position, -1):
            self.__a[i] = self.__a[i - 1]

        # Insert the new value in the right position
        self.__a[position] = item

        # Increase the number of elements
        self.__nItems += 1

      
if __name__ == "__main__":
    # Create an Array-object with space for 10 items
    array = Array(10)

    # Add a few items using the 'insert' method
    array.insert(1)
    array.insert(2)
    array.insert(3)

    # Test 'insert_at'
    print("Before insert at:")
    array.traverse()
    print()

    array.insert_at(0, 0) # Insert the element '0' at the start of the array
    array.insert_at(2, 9) # Insert the element '9' in the middle of the array
    array.insert_at(5, 7) # Insert the element '7' at the end of the array

    print("After insert at:")
    array.traverse()
    print()

    try:
        array.insert_at(-1, 5) # Trying to insert an element at a negative index
    except IndexError as e:
        print(f"Error: {e}")