# You have a hash table implemented with separate chaining.
# That means that collisions are handled by storing the 
# key-value pairs in a linked list at the index of the hash table.
# a) The hash table has a size of 11 and the following hash function:

# Key:              Hash value:
#--------------------------------
# "cornflakes"      7
# "fil"             5
# "potatis"         2
# "tomater"         5
# "mjölkchoklad"    4

# You have an empty hash table and the following keys are inserted:
# ("cornflakes", "1 paket")
# ("potatis", "2 kg")
# ("fil", "1 liter")
# ("tomater", "3 st")
# ("potatis", "3 kg")
# ("mjölkchoklad", "300 g")

# What does the hash table look like after all keys have been inserted?
# Answer: The hash table will look like this:

# Index:              Linked list:
#--------------------------------
# 0
# 1
# 2                    [("potatis", "2 kg"), ("potatis", "3 kg")]
# 3
# 4                    [("mjölkchoklad", "300 g")]
# 5                    [("fil", "1 liter"), ("tomater", "3 st")]
# 6
# 7                    [("cornflakes", "1 paket")]
# 8
# 9
# 10

# b) What is the complexity of inserting a key-value pair into the hash table?
# Answer: O(1) if there are no collisions, O(n) in the worst case if all 
# keys have the same hash value.