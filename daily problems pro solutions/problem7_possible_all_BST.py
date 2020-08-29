from functools import lru_cache

@lru_cache(maxsize=1000)
def possibleBst(n):
  if n<0:
    return 0
  elif n==1 or n==0:
    return 1

  possibilites=0

  for i in range(n):
    possibilites+=possibleBst(i)*possibleBst(n-1-i)
  return possibilites  

print(possibleBst(10))   
