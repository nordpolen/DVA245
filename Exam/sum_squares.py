# function: SUM_SQUARES(in_list) returns
# the sum of the squares of all elements in 
# in_list
#
# sum_squares <- 0
# for elem in in_list do
#    sum_squares <- sum_squares + elem^2
# return sum_squares

def sum_squares(in_list):
    sum_squares = 0
    for elem in in_list: # O(n)
        sum_squares += elem ** 2
    return sum_squares