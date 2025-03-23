# We have a priority queue class with the following methods:
# insert(priority, element) and
# remove() which removes and returns an element from the queue.

# Explain how you can use it to sort the list [12, 3, 5, 9, 4, 7].

# Answer: We can insert all elements into the priority queue with the element as the priority.
# Then we can remove all elements from the priority queue and insert them into a new list.

# Example:
# pq.insert(12, 12)
# pq.insert(3, 3)
# pq.insert(5, 5)
# pq.insert(9, 9)
# pq.insert(4, 4)
# pq.insert(7, 7)

# sorted_list = []
# while not pq.is_empty():
#     sorted_list.append(pq.remove())

# The sorted_list will be [3, 4, 5, 7, 9, 12].