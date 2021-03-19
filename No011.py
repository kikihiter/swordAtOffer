# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 210319
# @Author  : kiki
# @File    : No011.py
"""
第11题，找出旋转数组中的最小值
"""

# 测试项
test =[[1,6,11,16,21,-12,-3],[4,5,7,8,9,1,2,3],[1],[1,2],[2,1],[3,4,5,3],[1,0,1,1,1],[1,1,1,0,1],[0,1,1,1,1]]

# 核心代码
class Solution(object):
    def searchMin(self, nums):
        # 一个排序数组旋转后，会被分为两个排序数组，第一个排序数组中的所有元素都>=第二序列
        # 二分查找第二个排序数组的第一个数即为所求最小值
        left, middle, right = 0, 0, len(nums)-1
        while left < right:
            # 如果左端点比右端点小的话，则左端点已经移动到第二序列
            if nums[left] < nums[right]:
                return nums[left]
            else:
                middle = (left + right)>>1
                if nums[middle] > nums[right]:
                    left = middle + 1
                elif nums[middle] < nums[right]:
                    right = middle
                # 如果输入的数组不含重复数字的话，后面这一堆东西都可以省略
                elif nums[middle] == nums[right]:
                    if nums[left] > nums[middle]:
                        right = middle
                    else:
                    # left、middle、right三个指向的数字都相等，无法判断如何取舍
                        # 遍历这一部分，找到变小的那个数字，返回之
                        for i in range(left,right):
                            if nums[i+1] < nums[i]:
                                return nums[i+1]
                        # 遍历完，发现所有数字都是一样的，随便返回一个
                        else:
                            return nums[left]
                               
        return nums[left]

# 输出显示
if __name__ == "__main__":
    A = Solution()
    for nums in test:
        print (A.searchMin(nums))