class node:
  def __init__(self,data=None):
    self.data=data
    self.next=None

class linked_list:
  def __init__(self):
    self.head=node()

  def append(self,data):
    new_node=node(data)
    if self.head.data==None:
      self.head=new_node
    else:
      cur=self.head
      while cur.next!=None:
        cur=cur.next
      cur.next=new_node

  def display(self):
    cur=self.head
    while cur!=None:
      print(cur.data,end=" ")
      cur=cur.next


def resultant_linked_list(l):
  cur=l.head
  sum=0
  d={0:node()}
  a=[]
  while cur!=None:
    sum+=cur.data
    if sum not in d:
      d[sum]=cur
      a.append(sum)
    else:
      while len(a)!=0 and a[-1]!=sum:
        del d[a[-1]]
        a.pop()
      d[sum].next=cur.next 
    cur=cur.next  
  if d[0].next==None and sum==0:
    l.head=d[0]  
  elif d[0].next!=None:
    l.head=d[0].next
  return l


l=linked_list()
data=list(map(int,input().split()))
for i in data:
  l.append(i)
resultant_linked_list(l)
l.display()    






            



