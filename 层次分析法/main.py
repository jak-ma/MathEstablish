import numpy as np

# A = np.array([[1,2,3,5],[1/2,1,1/2,2],[1/3,2,1,2],[1/5,1/2,1/2,1]])
A = np.array([[1,1/5,3],[5,1,6],[1/3,1/6,1]])
# print(A)
# todo shape[] 获取A的形状信息
# r = A.shape[0]      # todo 0获取A的行
l = A.shape[1]      # todo 1获取A的列
# print(r)
# print(l)
# todo 求最大特征值以及对应的特征向量：
# np.linalg.eig 是numpy中的一个库函数
# 用于计算方阵的特征值和特征向量
# eig_val 值 | eig_vec 向量
eig_val,eig_vec = np.linalg.eig(A)
# print(eig_val,eig_vec)
Max_eig_val = np.max(eig_val)
# print(Max_eig_val)
# 一致性指标 CI
CI = (Max_eig_val - l)/(l - 1)
print(CI)
# todo -RI-的值有时候要考虑除0问题，所以需要规范为一个很小的数值,如下矩阵中的第二个元素 0.0001
RI = [0,0.0001,0.52,0.89,1.12,1.26,1.36,1.41,1.46,1.49,1.52,1.54,1.56,1.58,1.59]
CR = CI / RI[l-1]   # 一致性比例 CR
print(CR)
# todo !!! CR < 0.1, 一致性可以接受：CR > 0.1，需要修改判断矩阵
# 一致性检验通过后，根据判断矩阵 计算权重

