# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Adapted for DVA245 by Anna Friebe

import random

def merge(S1, S2, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] <= S2[j]):
            S[i+j] = S1[i]      # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]      # copy jth element of S2 as next item of S
            j += 1


def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return                # list is already sorted
    # divide
    mid = n // 2
    S1 = S[0:mid]           # copy of first half
    S2 = S[mid:n]           # copy of second half
    # conquer (with recursion)
    merge_sort(S1)          # sort copy of first half
    merge_sort(S2)          # sort copy of second half
    # merge results
    merge(S1, S2, S)        # merge sorted halves back into S


if __name__ == '__main__':
    in_list1 = [1, 2, 5, 8, 9]
    in_list2 = [2, 3, 6, 7, 9]
    # correct size for output list
    merged_list1 = [0]*10
    merge(in_list1, in_list2, merged_list1)
    merged_result = [1, 2, 2, 3, 5, 6, 7, 8, 9, 9]
    if merged_result == merged_list1:
        print("first merge ok")
    else:
        print("first merge failed")
    in_list1 = [1, 2, 5, 8, 9]
    in_list2 = [2, 3, 6, 7, 9]
    # correct size for output list
    merged_list2 = [0]*10
    merge(in_list1, in_list2, merged_list2)
    if merged_result == merged_list2:
        print("second merge ok")
    else:
        print("second merge failed")
    # create two lists with elements 0-99, randomly reordered
    orig_list1 = random.sample(range(100), 100)
    orig_list2 = random.sample(range(100), 100)
    # combine them into one list with 200 elements
    orig_list1.extend(orig_list2)
    merge_sort(orig_list1)
    error_indices = []
    for i in range(100):
        ind1 = i*2
        if orig_list1[ind1] != i:
            error_indices.append(ind1)
        ind2 = ind1+1
        if orig_list1[ind2] != i:
            error_indices.append(ind2)
    if len(error_indices) == 0:
        print("merge sort passed") 
    else:
        print("merge sort failed, errors in indices: ", error_indices)
        
