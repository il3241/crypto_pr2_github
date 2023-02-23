import numpy as np

print(676%26)
print(731%26)
print(638%26)
matrix_key = []

for i in range(5):
    tp = list(map(int, input().split()))
    matrix_key.append(tp)

matrix_key = np.array(matrix_key)
print(round(np.linalg.det(matrix_key))%26, 'l')

"""matrix_key = []

    for i in range(3):
        tp = list(map(int, input().split()))
        matrix_key.append(tp)

    matrix_key = np.array(matrix_key)

    rev = find_rev(matrix_key, 3)

    encrypt('aaaa',3,find_rev(matrix_key, 3))"""
""" matrix_key1 = []

 for i in range(3):
     tp = list(map(int, input().split()))
     matrix_key1.append(tp)

 matrix_key1 = np.array(matrix_key1)

 qq = np.array(find_rev(matrix_key1, 3))
 print(qq, 223)

 print(decrypt(list("zmnvcxfowhae"), 3, qq))"""