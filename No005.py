# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 210318
# @Author  : kiki
# @File    : No004.py
"""
二维数组搜索
"""
# 测试项
test =[[[1,6,11,16,21],
        [2,7,12,17,22],
        [3,8,13,18,23],
        [4,9,14,19,24],
        [5,10,15,20,25]]]

# 核心代码
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or len(matrix)<1 or len(matrix[0])<1:
            return False
        i, j = 0, len(matrix[0])-1
        # 从右上角开始进行比较
        while i < len(matrix) and j > -1:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
        return False


# 输出显示
A = Solution()
target = 5
for matrix in test:
    print (A.searchMatrix(matrix,target))