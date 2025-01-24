import ArrayLab1
maxSize = 10                    # Max size of the array
arr = ArrayLab1.Array(maxSize)      # Create an array object
   
arr.insert(77)                  # Insert 5 items
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

print("Array containing", len(arr), "items")
arr.traverse()

print("Search for 12 returns", arr.search(12))

print("Search for 12.34 returns", arr.search(12.34))

print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))

print("Array after deletions has", len(arr), "items")
arr.traverse()

# TODO: implement tests for insert_at
# test for insertion 1) at the beginning
# 2) at the end
# 3) at a position that is not in beginning or end

# you can implement this test in a main function in the ArrayLab1.py file
# or in a separate file