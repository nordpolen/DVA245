def fun(item, sorted_list):
    lo = 0
    hi = len(sorted_list) - 1
    while lo <= hi: 
        mid = (lo + hi) // 2
        if sorted_list[mid] == item:
            return True
        elif sorted_list[mid] < item:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

# a) fun(12, [1, 3, 5, 7, 9, 12, 17, 20])
#       1) 
#       2)
#
#
#
#
#
#
#
# b) fun(2, [1, 3, 5, 7, 9, 12, 17, 20])
# 
#
#
#
#
#
#
#
# c) 
# 
#
#
#
#
#
#
#
# d) 
# 
#
#
#
#
#
#
#