from my_package import vec_alg, vec_linalg

A = [1, 2]
B = [3, 4]

print(
    vec_alg.vec_mul(A, B),
    vec_alg.vec_mul_n(A, 2),
    vec_linalg.vec_len(A)
)
