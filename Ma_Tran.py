import numpy as np
A=np.array([[1,2,3],[2,3,4],[4,5,6]])
B=np.array([[6,7,8],[7,8,9],[8,9,10]])
print("Ma trận A:",A)
print("Ma trận B:",B)
print('Tổng 2 ma trận =',A+B)
print('Tích 2 ma trận =',A.dot(B))
print('Chuyển vị của ma trận A:',A.transpose())
print('Chuyển vị của ma trận B:',B.transpose())