from math import sqrt

def vec_dot(A, B):
    return A[0] * B[0] + A[1] * B[1]

def vec_len(A):
    return sqrt(A[0]**2 + A[1]**2)
