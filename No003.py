# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 210317
# @Author  : kiki
# @File    : No003.py
"""
找到数组中的重复数字
"""
# 测试项
test = [[2,3,1,0,2,5,3],[],[1,2,3,4,5,0],[1,3,1,4,5,6,0,1,3,4],[0,1,2,3,5,5,5],[0,1,2,3,5,1,0]]

# 逻辑代码
class Solution(object):
    def findNum(self, array):
        i = 0
        while 0 <= i < len(array):
            # 当前位置已经调整好
            if i == array[i]:
                i += 1
                continue
            # 当前位置未调整好
            while i != array[i]:
                num = array[i]
                # 找到num应该在的位置，发现相等
                if array[num] == array[i]:
                    return num
                # 将num放到其应该在的位置，将原本在num位置的数据移到索引i位置，继续这个过程
                array[num], array[i] = array[i], array[num]
                # print (array)
            i += 1
            
# 输出显示
A = Solution()
for array in test:
    print (A.findNum(array))
    
    