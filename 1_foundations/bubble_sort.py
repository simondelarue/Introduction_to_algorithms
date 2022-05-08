"""
Created on May 2022
@author: Simon Delarue <sdelarue@enst.fr>
"""

def bubble_sort(arr):
    ''' Bubble sort algorithm. 
    
    Parameters
    ----------
        arr: input array

    Output
    ------
        Sorted array.
    '''

    n = len(arr)

    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        
    return arr
