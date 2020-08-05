import scipy as sp

N = 5

A = sp.rand(N,N)
B = sp.rand(N,N)
A = sp.matrix(sp.rand(N,N))
B = sp.matrix(sp.rand(N,N))

print(f"A = \n{A}")
print(f"B = \n{B}")

C = A*B

print(f"C = \n{C}")

print(f"C00 = \n{C[0,0]}")
print(f"A00 * B00 = \n{A[0,0]*B[0,0]}") 