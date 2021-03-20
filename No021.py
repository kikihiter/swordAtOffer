# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 210320
# @Author  : kiki
# @File    : No021.py
"""
第21题，奇偶分组
"""

# 测试项
test = [[1,2,3,4,5,6,6,7,8],[1,3,5,7,9,11],[1],[],[2,4,6,8,10],[2,1],[1,1],[1,1,1],[0,0,1],[1,0,0],[0,1,0],[13,674,8,54,6,5,35,65,65,5,356,3,5,6,356,2,5,6,5,3,56,5,6,56,35,63,5,3,56,67,58,9,5,59,6896,5,3,63,56,7,6,85,78],
        [-12,-67,-5],[-1],[-1,0,1,-1]]

# 核心代码
class Solution(object):
    # 为了满足书中提出的可拓展性，可以用于基于其他条件的分组，条件封装为函数
    # 判断数字是否为奇数
    def isOdd(self, num):    
        return num&1 == 1
    
    # 判断数字是否为负数
    def isNeg(self, num):
        return n < 0
    
    def grouping(self, nums):
        """
        nums为待分组的数组
        """
        left, right = 0, len(nums)-1    # 两端点的指针
        # 用两指针遍历数组
        while left < right:
            # 调用条件判断函数，符合条件的数字不动，左指针右移
            if self.isOdd(nums[left]):
                left += 1
            # 不符合条件的数字在右侧，也不需要动，右指针左移
            if not self.isOdd(nums[right]):
                right -= 1
            # 当左右两个数字需要调换时，调换两个数字，并将两个指针向中间移动
            if self.isOdd(nums[left]) == False and self.isOdd(nums[right]) == True:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return nums
        



# 输出显示
if __name__ == "__main__":
    A = Solution()
    for nums in test:
        print (A.grouping(nums))