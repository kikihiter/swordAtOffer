# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 210319
# @Author  : kiki
# @File    : No011.py
"""
第11题，找出旋转数组中的最小值
"""

# 测试项
test =[[1,6,11,16,21,-12,-3],[4,5,7,8,9,1,2,3],[1],[1,2],[2,1],[3,4,5,3]]

# 核心代码
class Solution(object):
    def searchMin(self, nums):
        # 二分查找
        left, middle, right = 0, 0, len(nums)-1
        while left < right:
            middle = (left + right)>>1
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        return nums[left]

# 输出显示
if __name__ == "__main__":
    A = Solution()
    for nums in test:
        print (A.searchMin(nums))