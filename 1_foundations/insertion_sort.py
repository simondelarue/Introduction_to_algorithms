"""
Created on May 2022
@author: Simon Delarue <sdelarue@enst.fr>
"""

def insertion_sort(arr):
    ''' Insertion sort algorithm. 
    
    Parameters
    ----------
        arr: input array
    '''
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # insert arr[i] in the sorted subarray arr[0:i-1]
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        
    return arr
