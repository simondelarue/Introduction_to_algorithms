"""
Created reated on May 2022
@author: Simon Delarue <sdelarue@enst.fr>
"""

def split(A, n):
    ''' Split matrix A into submatrices of size n. '''

    A11 = A[:n, :n]
    A12 = A[:n, n:]
    A21 = A[n:, :n]
    A22 = A[n:, n:]
    
    return A11, A12, A21, A22

def strassen(A, B, n) 
    ''' Matrix multiplication using Strassen algorithm. 

	Parameters
	----------
		A, B: square matrices
		n: size of matrices A and B.'''
	
	# Base case
    if n == 1:
        return A * B
    
    # Divide
    idx = int(n/2)
    A11, A12, A21, A22 = split(A, idx)
    B11, B12, B21, B22 = split(B, idx)
    
    # Conquer
    P1 = Strassen(A11, B12 - B22, n/2)
    P2 = Strassen(A11 + A12, B22, n/2)
    P3 = Strassen(A21 + A22, B11, n/2)
    P4 = Strassen(A22, B21 - B11, n/2)
    P5 = Strassen(A11 + A22, B11 + B22, n/2)
    P6 = Strassen(A12 - A22, B21 + B22, n/2)
    P7 = Strassen(A11 - A21, B11 + B12, n/2)

    C = np.zeros((int(n), int(n)))
    C[:idx, :idx] = P5 + P4 - P2 + P6
    C[:idx, idx:] = P1 + P2
    C[idx:, :idx] = P3 + P4
    C[idx:, idx:] = P5 + P1 - P3 - P7
    
    return C
    
