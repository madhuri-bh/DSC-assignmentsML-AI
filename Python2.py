from collections import Counter

n = input("Enter total number of gloves")

print("Enter colors of array")
  
 
ar = list(map(int,input().split()))

pairs = 0

n = Counter(ar)
for i in n.values():
    
pairs += (i//2)
         

print(pairs)