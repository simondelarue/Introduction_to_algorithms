"""
Created on May 2022
@author: Simon Delarue <sdelarue@enst.fr>
"""

def selection_sort(arr):
    ''' Selection sort algorithm.
    
    Parameters
    ----------
        arr: input array.
    '''
    n = len(arr)
    
    for i in range(0, n):
        smallest = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j
        # Swap found minimum with first element
        arr[i], arr[smallest] = arr[smallest], a[i]
        
    return arr
