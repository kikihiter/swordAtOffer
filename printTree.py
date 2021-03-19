# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 210318
# @Author  : kiki
# @File    : printTree.py
"""
二叉树的可视化，将一个二叉树按层序输出
"""

def PTi(root):
    stack = [root]
    temp = []
    while stack != [] or temp != []:
        while stack != []:
            root = stack.pop(0)
            print (root.val, end=' ')
            if root.left:
                temp.append(root.left)
            if root.right:
                temp.append(root.right)
        print ('\n')
        stack = temp
        temp = []


def PTNone2X(root):
# 用X来代替空节点，便于观察节点连接信息
    stack = [root]
    temp = []
    while stack != [] or temp != []:
        while stack != []:
            root = stack.pop(0)
            if root == 'X':
                print ('X', end=' ')
                continue
            print (root.val, end=' ')
            if root.left:
                temp.append(root.left)
            else:
                temp.append('X')
            if root.right:
                temp.append(root.right)
            else:
                temp.append('X')
        print ('\n')
        stack = temp
        temp = []

def PT(root):
    ptList = []
    stack = [[root,0,0]]
    # root, i, j 分别代表节点，和节点所在的行列，i即是深度-1，j为满元素情况下节点所应该在的位置，空节点用' '代替
    # 用栈遍历根节点，计算每一个节点的i、j值，并添加进ptList数组中
    while stack != []:
        root, i, j = stack.pop()
        # 深度大于ptList的值了，创建新的一行
        if len(ptList) < i+1:
            temp = ['.' for _ in range(2**i)]
            ptList.append(temp)
        ptList[i][j] = root.val # 当前节点信息存入ptList中
        if root.left:
            stack.append([root.left, i+1, 2*j])
        if root.right:
            stack.append([root.right, i+1, 2*j+1])
            
    print (ptList)
    # 以特定格式打印ptList列表
    l = len(ptList)
    for i in range(l):
        for num in ptList[i]:
            t = (2**(l-i-1)*3-1)
            print(' '*int(t/2), end = '')
            print(num, end = '')
            if t%2 != 0:
                t = t+1
            print(' '*int(t/2), end = '')
        print('|','\n')
            
    
        
# 树的基本节点
# class treeNode(object):
    # def __init__(self, x):
        # self.val = x
        # self.left = None
        # self.right = None


# root = treeNode(0)
# print (root.val, end = '')
# PT(root)