# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 210318
# @Author  : kiki
# @File    : No007.py
"""
由二叉树的先序遍历和中序遍历来建树
"""
import printTree
import printTreeO


# 测试项
test =[[[1,2,4,7,3,5,6,8],
        [4,7,2,1,5,3,8,6]]]

# 树的基本节点
class treeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 核心代码
class Solution(object):
    def buildTree(self, xianXu, zhongXu):
        """
        这个函数返回由xianXu和zhongXu两个数组决定的二叉树的根节点
        xianXu和zhongXu均为整型的列表，长度一致
        """
        # 如果传入为空，或者不含元素时，直接返回空
        if not xianXu or len(xianXu) == 0:
            return None
        # 创建根节点
        rootVal = xianXu[0]
        root = treeNode(rootVal)
        # 找到根节点左侧所含的数字
        i = 0
        while i < len(zhongXu):
            if zhongXu[i] == xianXu[0]:
                break
            i += 1
        root.left = self.buildTree(xianXu[1:i+1], zhongXu[:i])
        root.right = self.buildTree(xianXu[i+1:], zhongXu[i+1:])
        # printTree.PT(root)
        return root


# 输出显示
A = Solution()
for testList in test:
    xianXu, zhongXu = testList
    root = A.buildTree(xianXu,zhongXu)
    printTree.PT(root)
    printTree.PTNone2X(root)
    # printTreeO.PTO(root)
    printTree.PTi(root)