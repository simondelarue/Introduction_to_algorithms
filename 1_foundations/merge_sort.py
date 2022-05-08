"""
Created on May 2022
@author: Simon Delarue <sdelarue@enst.fr>
"""


def merge(arr, p, q, r):
    ''' Merges two (sorted) subarrays, respectively arr[p:q+1] and arr[q:r] into a single sorted subarray arr[p:r]. 
    
    Parameters
    ----------
        arr: input array.
        p, q, r: indices such that p <= q < r
    '''
    n_l = q - p + 1
    n_r = r - q
    
    # Copy to left and right arrays
    arr_r = [0] * (n_l)
    arr_l = [0] * (n_r)
    for i in range(n_l):
        arr_r[i] = arr[p+i]
    for j in range(n_r):
        arr_l[j] = arr[q+1+j]

    # As long as each of the left and right subarrays contain unmerged elements,
    # copy the smallest unmerged element into arr[p:r]
    i, j = 0, 0
    k = p
    while i < n_l and j < n_r:
        if arr_l[i] <= arr_r[j]:
            arr[k] = arr_l[i]
            i += 1
        else:
            arr[k] = arr_r[j]
            j += 1
        k += 1
    
    # Having gone through one of left or right subarray entirely, copy
    # the remainder of the other to the end of arr[p:r]
    while i < n_l:
        arr[k] = arr_l[i]
        i += 1
        k += 1
    while j < n_r:
        arr[k] = arr_r[j]
        j += 1
        k += 1


def merge_sort(arr, p, r):
    ''' Merge sort algorithm. 
    
    Parameters
    ----------
        arr: input array.
        p, r: start and end indices of array arr.
    '''
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)
