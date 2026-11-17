import numpy as np

hours = np.arange(0, 22, 3)
line = np.linspace(0, 1, 5)
zeros = np.zeros(6, dtype=int)
unknown_table = np.full((2, 3), -1)
identity = np.eye(3)

print(hours)
print(hours.shape, hours.ndim, hours.size, hours.dtype)
print(line)
print(zeros)
print(unknown_table)
print(identity)

print(hours[2])
print(hours[-1])
print(hours[2:6])
print(hours[::2])
print(hours[::-1])

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18],
])

print(temperatures.shape, temperatures.ndim, temperatures.size)
print(temperatures[1, 2])
print(temperatures[0])
print(temperatures[:, -1])
print(temperatures[:2, 1:])
print(temperatures[0:2, 1:3])

matrix = np.arange(1, 26).reshape(5, 5)

p1 = matrix[:3]
print(p1, p1.shape)

p2 = matrix[3:]
print(p2, p2.shape)

p3 = matrix[:, :2]
print(p3, p3.shape)

p4 = matrix[1:4, 2:5]
print(p4, p4.shape)

p5 = matrix[3:, 3:]
print(p5, p5.shape)

vector = np.array([10, 20, 30, 40, 50])
vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1:, 1:] = 9

changed_hours = hours.copy()
changed_hours[2:5] = 99
changed_hours[1::2] = -1

print(changed_hours)
print(hours)

changed_matrix = matrix.copy()
changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100
print(changed_matrix)
print(matrix)


numbers = np.arange(12)
table = numbers.reshape(3, 4)
transposed = table.T

print(numbers.shape)
print(table.shape)
print(transposed.shape)
