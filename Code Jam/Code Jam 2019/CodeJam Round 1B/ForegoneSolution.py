from random import randint

#Read input
t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
  n = int(input())
  while(True):
      x = randint(1,n-1)
      if ('4' in str(x)) or ('4' in str(n-x)):
          continue
      else:
          break
  #Print Solution
  print("Case #{}: {} {}".format(i,x,n-x))
