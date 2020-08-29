'''Hi, here's your problem today. This problem was recently asked by Apple:

Given a binary tree, return the list of node values in zigzag order traversal. Here's an example

Input:
        1
      /   |
     2     3
    / \   /  |
   4   5 6   7

 Output: [1, 3, 2, 4, 5, 6, 7]'''




class node:
  def __init__(self,data=None,left=None,right=None):
    self.data=data
    self.left=left
    self.right=right

class BinaryTree:
  def __init__(self):
    self.root=None

  def zigzag_traversal(self,root):
    curr_arr=[]
    next_arr=[] 

    curr_arr.append(root) 

    isLtoR=True

    while curr_arr:
      temp=curr_arr.pop(-1)
      print(temp.data,end=" ")
      if isLtoR:
        if temp.left:
          next_arr.append(temp.left)
        if temp.right:
          next_arr.append(temp.right) 
      else:
        if temp.right:
          next_arr.append(temp.right) 
        if temp.left:
          next_arr.append(temp.left)

      if len(curr_arr)==0:
        isLtoR=not(isLtoR)
        curr_arr,next_arr=next_arr,curr_arr

BTree=BinaryTree()
n4 = node(4)
n5 = node(5)
n6 = node(6)
n7 = node(7)
n2 = node(2, n4, n5)
n3 = node(3, n6, n7)
n1 = node(1, n2, n3)
BTree.root=n1
BTree.zigzag_traversal(BTree.root)          