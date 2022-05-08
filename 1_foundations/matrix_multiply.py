"""
Created on May 2022
@author: Simon Delarue <sdelarue@enst.fr>
"""

def matrix_multiplication(A, B, C, n):
	''' Naïve matrix multiplication.

	Parameters
	----------
		A, B: square matrices
		C: square matrix storing result
		n: size of matrix A, B and C
	'''

	for i in range(n):
		for j in range(n):
			for k in range(n):
				C[i, j] += A[i, k] * B[k, j]
				
	return C
