from functools import lru_cache

class newNode:  
  def __init__(self, item):
    self.key=item 
    self.left = None
    self.right =None

def preorder(root):
  if (root != None) : 
    print(root.key, end = " " ) 
    preorder(root.left)  
    preorder(root.right) 

@lru_cache(maxsize=1000)
def constructTrees(start, end):
  list = []  
  if (start > end) : 
    list.append(None)  
    return list
  
  for i in range(start, end + 1):  
    leftSubtree = constructTrees(start, i - 1)  
    rightSubtree = constructTrees(i + 1, end)  
    for j in range(len(leftSubtree)) : 
      left = leftSubtree[j]  
      for k in range(len(rightSubtree)):  
          right = rightSubtree[k]  
          node = newNode(i)   
          node.left = left   
          node.right = right 
          list.append(node) 
  return list

 
  
if __name__ == '__main__': 

  n=int(input())
  totalTreesFrom1toN = constructTrees(1, n)  

  print("Preorder traversals of all constructed BSTs are")  
  for i in range(len(totalTreesFrom1toN)):  
      preorder(totalTreesFrom1toN[i]) 
      print()        