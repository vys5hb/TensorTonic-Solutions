import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    res = np.zeros((len(A[0]), len(A)))
    for i in range(len(A[0])):
        for j in range(len(A)):
            res[i, j] = A[j][i]
    return res
    
