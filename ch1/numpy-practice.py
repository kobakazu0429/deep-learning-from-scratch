import numpy as np

# vector
x = np.array([1.0, 2.0, 3.0])
y = np.array([2.0, 4.0, 6.0])
print(x)
print(y)
# print(type(x))
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x / 2)

# matrix
A = np.array([[1, 2], [3, 4]])
B = np.array([[3, 0], [0, 6]])
print(A)
print(A.shape)
print(A + B)
print(A * B)

# broadcast
A = np.array([[1, 2], [3, 4]])
B = np.array([10, 20])
#  (1 2)(10) { = (1 2)(10 20) } = (10 40)
#  (3 4)(20) { = (3 4)(10 20) } = (30 80)
print(A * B)

# access to tensor
X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
print(X.flatten()[np.array([0, 2, 4])])

print(X > 15)
print(X[X > 15])
