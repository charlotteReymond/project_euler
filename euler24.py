#euler 24
somme=0
from itertools import permutations
perm = permutations([0,1,2,3,4,5,6,7,8,9])                         

for i in list(perm) :
   somme+=1
   if somme == 1000000:
         print(i)
