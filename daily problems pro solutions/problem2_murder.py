#input [3,6,3,4,1]
#output 3
#explanation only [6,4,1] were able to see in front of them.
def witnesses(heights):
  count=1
  for i in range(len(heights)-2,-1,-1):
    for j in range(len(heights)-1,i-1,-1):
      if heights[i]<=heights[j]:
        break
      if i==j-1:count+=1
      
  return count  
print(witnesses([3,6,3,1,4]))     
