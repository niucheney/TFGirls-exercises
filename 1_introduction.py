#encoding:utf-8
#为了和python3 兼容，如果逆使用的python 2.7
from __future__ import print_fuction, division
import tensorflow as tf
print('Loaded TF version',tf.__version__)
#Tensor是张量
#标量表示值
#矢量表示位置（空间中的点）

#一维数组是矢量
#多维数组是张量，矩阵也是张量

#4个重要的类型
# @Variable 计算图谱中的变量
# @Tensor 一个多维矩阵，带有很多方法。
# @Graph 一个计算图谱
# @Session 用来运行一个计算图谱。

# 三个重要函数
# variable constant placeholder
