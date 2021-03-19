# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 210317
# @Author  : kiki
# @File    : No004.py
"""
找到数组中的重复数字
"""
# 测试项
test = [[2,3,1,1,2,5,3],[1,2,3,4,5,1],[1,3,1,4,5,6,1,1,3,4],[5,1,2,3,5,5,5],[5,1,2,3,5,1,0],[]]


class Solution:
    def findDuplicate(self, nums):
        slow = fast = cir_start = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break

        while True:
            slow = nums[slow]
            cir_start = nums[cir_start]
            if cir_start == slow:
                return slow

# 输出显示
A = Solution()
for array in test:
    print (A.findDuplicate(array))