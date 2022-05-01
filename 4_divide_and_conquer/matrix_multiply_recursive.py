"""
Created reated on April 2022
@author: Simon Delarue <sdelarue@enst.fr>
"""

def split(A, n):
    ''' Split matrix A into submatrices of size n. '''

    A11 = A[:n, :n]
    A12 = A[:n, n:]
    A21 = A[n:, :n]
    A22 = A[n:, n:]
    
    return A11, A12, A21, A22

def matrix_multiplication_recursive(A, B, C, n):
    ''' Recursive matrix multiplication. 

	Parameters
	----------
		A, B: square matrices
		C: square matrix to store result
		n: size of matrices A, B and C
	'''
    
    # Base case
    if n == 1:
        C[0, 0] += A[0, 0] * B[0, 0]
        return 
                
    # Divide
    idx = int(n/2)
    A11, A12, A21, A22 = split(A, idx)
    B11, B12, B21, B22 = split(B, idx)
    
    # Conquer
    matrix_multiplication_recursive(A11, B11, C[:idx, :idx], n/2)
    matrix_multiplication_recursive(A12, B21, C[:idx, :idx], n/2)
    matrix_multiplication_recursive(A11, B12, C[:idx, idx:], n/2)
    matrix_multiplication_recursive(A12, B22, C[:idx, idx:], n/2)
    matrix_multiplication_recursive(A21, B11, C[idx:, :idx], n/2)
    matrix_multiplication_recursive(A22, B21, C[idx:, :idx], n/2)
    matrix_multiplication_recursive(A21, B12, C[idx:, idx:], n/2)
    matrix_multiplication_recursive(A22, B22, C[idx:, idx:], n/2)

    return C
