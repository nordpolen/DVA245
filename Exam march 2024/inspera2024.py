
# O(1) + O(N) + O(1) results in O(N) that grows fastest 
def count_items(in_list, item):
    # O(1) here
    n_items = 0
    # O(n) - we loop over all elements in in_list
    for elem in in_list:
        # O(1) inside loop, does not depend on length of in_list
        if elem == item:
            n_items += 1
    # O(1) for return
    return n_items

if __name__=='__main__':
    test_list = [5, 8, 2, 4, 5, 7, 5]
    print(count_items(test_list, 5))