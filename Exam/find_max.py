def find_max(in_list):
    cur_max = in_list[0] # O(1)
    for i in range(1, len(in_list)):
        if in_list[i] > cur_max:
            cur_max = in_list[i]
    return cur_max

# Time complexity: O(n)