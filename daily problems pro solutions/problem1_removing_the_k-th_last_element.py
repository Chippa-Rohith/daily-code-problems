import linked_list_ref as link
#input[1,2,3,4,5] ,3
#output[1,2,4,5]
n=[1,2,3,4,5]
k=6
l=link.linked_list()
for i in n:
  l.append(i)
def remove_kth_ele(ls,k):
  if k>ls.lenght():
    print("invalid kth position")
    return
  cur=ls.head
  prev=None
  i=0
  while i!=k:
    prev=cur
    cur=cur.next
    i+=1
  prev.next=cur.next
  return
remove_kth_ele(l,k)
l.display() 


