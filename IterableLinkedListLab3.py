# Listings from chapter 5

# Note: Links are often referred to as nodes
#
# using lower_case instead of mixedCase for functions and variables
# __str__using __iter__

class Link:
    __slots__=('__data', '__next')

    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next

    def get_data(self):
        return self.__data
    
    def set_data(self, data):
        self.__data = data

    def get_next(self):
        return self.__next
    
    def set_next(self, link):
        self.__next = link

    def is_last(self):
        return self.__next is None
    
    def __str__(self):
        return str(self.get_data())
    
def identity(x):
    return x
    
class LinkedList:
    def __init__(self):
        self.__first = None

    def get_first(self):
        return self.__first
    
    def set_first(self, link):
        if link is None or isinstance(link, Link):
            self.__first = link
        else:
            raise RuntimeError("First link must be Link or None")
        
    def get_next(self):
        return self.get_first()
    
    def set_next(self, link):
        self.set_first(link)

    def is_empty(self):
        return self.__first is None

    def first(self):
        if self.is_empty():
            raise RuntimeError("No first item in empty list")
        return self.get_first().get_data()
    
    # ------------------------
    # ADDED: 2025-09-07, Josefina
    # Method to insert an element at a specific position in the linked list, and a main function to test it
    # ------------------------

    # def __iter__(self):
    #     link = self.get_first()
    #     while link:
    #         yield link.get_data()
    #         link = link.get_next()´

    def iter_recursive(self, link):
        if link:
            yield link.get_data()
            yield from self.iter_recursive(link.get_next()) 
        return

    def __iter__(self):
        return self.iter_recursive(self.get_first())

    # def __len__(self):
    #     length = 0
    #     link = self.get_first()
    #     while link:
    #         length += 1
    #         link = link.get_next()
    #     return length

    def len_recursive(self, link):
        if link:
            return 1 + self.len_recursive(link.get_next()) 
        return 0

    def __len__(self):
        return self.len_recursive(self.get_first())
    
    def __str__(self):
        result = "["
        for elem in self:     # using __iter__
            if len(result) > 1:
                result += " > "
            result += str(elem)
        return result + "]"
    
    def insert(self, data):
        # create a new Link with next referencing the list's current first 
        link = Link(data, self.get_first())
        self.set_first(link)

    # def find(self, goal, key=identity):
    #     link = self.get_first()
    #     while link:
    #         if key(link.get_data()) == goal:
    #             return link
    #         link = link.get_next()

    def find_recursive(self, link, goal, key):
        if link is None:
            return None
        if key(link.get_data()) == goal:
            return link
        return self.find_recursive(link.get_next(), goal, key) 

    def find(self, goal, key=identity):
        return self.find_recursive(self.get_first(), goal, key) 
        
    def search(self, goal, key=identity):
        link = self.find(goal, key)
        if link is None:
            return False
        return link.get_data()
    
    def insert_after(self, goal, new_data, key=identity):
        link = self.find(goal, key)
        if link is None:
            return False
        # create a new Link with next referencing link's next
        new_link = Link(new_data, link.get_next())
        # update link's next to reference the new link
        link.set_next(new_link)
        return True
    
    def delete_first(self):
        if self.is_empty():
            raise RuntimeError("Cannot delete first of empty list")
        first = self.get_first()
        self.set_first(first.get_next())
        return first.get_data()    # Return data of deleted link
        

    # # changed to use previous and current, a little more clear
    # def delete(self, goal, key=identity):
    #     if self.is_empty():
    #         raise RuntimeError("Cannot delete from empty list")
    #     # Link before goal link
    #     # At first LinkedList (self), works because we implemented 
    #     # get_next and set_next for LinkedList
    #     previous = self
    #     current = self.get_next()
    #     # We need to track previous to update the next reference at deletion
    #     while current:
    #         if goal == key(current.get_data()): # Found the link to delete
    #             previous.set_next(current.get_next())
    #             return current.get_data()  # Return data of deleted link
    #         previous = current       # step to check next link
    #         current = current.get_next()
    #     # goal not found, raise exception
    #     raise RuntimeError("No item with matching key found in list")

    def delete_recursive(self, previous, current, goal, key):
        if current is None:
            raise RuntimeError("No item with matching key found in list")
        if goal == key(current.get_data()):
            previous.set_next(current.get_next()) 
            return current.get_data() 
        return self.delete_recursive(current, current.get_next(), goal, key) 

    def delete(self, goal, key=identity):
        if self.is_empty():
            raise RuntimeError("Cannot delete from empty list")
        return self.delete_recursive(self, self.get_next(), goal, key) 
    

if __name__ == '__main__':
    # test link
    link = Link(3)
    print("link, get_data()==3", link.get_data() == 3)
    print("link, get_next() is None", link.get_next() is None)
    linked_list = LinkedList()
    print("linked_list is_empty()", linked_list.is_empty())
    print("linked_list get_first is None", linked_list.get_first() is None)
    print("len(linked_list) == 0", len(linked_list) == 0)
    linked_list.set_first(link)
    print("linked_list get_first().get_data() == 3", linked_list.get_first().get_data()==3)
    print("len(linked_list) == 1", len(linked_list) == 1)
    for i in range(5, 10):
        linked_list.insert(i)
    print("linked_list after insertions: ", str(linked_list))
    print("len(linked_list) == 6", len(linked_list) == 6)

    for i in range(0, 3):
        print("search returned False:", linked_list.search(i) == False)
    for i in range(5, 10):
        print("search returned data", linked_list.search(i) == i)

    linked_list.insert_after(5, 4)
    linked_list.insert_after(3, 2)
    print("linked_list after insert_after calls: ", str(linked_list))

    linked_list.delete_first()
    print("len(linked_list)==7", len(linked_list) == 7)
          
    linked_list.delete(5)
    linked_list.delete(2)
    # test removing the first
    linked_list.delete(8)
    try:
        linked_list.delete(2)
        print("No exception raised.")
    except:
        print("Exception raised as expected.")
    print("len(linked_list)==4", len(linked_list) == 4)
    print("linked_list after deletions: ", str(linked_list))
    for i in [2, 5, 8, 9]:
        print("search returned False:", linked_list.search(i) == False)
    

    # Test deleting from an empty list
    empty_list = LinkedList()
    try:
        empty_list.delete(1)
    except RuntimeError:
        print("Correctly raised an error on deleting from an empty list.")