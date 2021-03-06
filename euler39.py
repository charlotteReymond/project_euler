#euler 39
import math
liste = set()
lpg=5

def nbrsolution(n):
   liste.clear()
   carré=int(n/2)
   for a in range(1,carré+1):
      for b in range(1,carré+1):
         for c in range(1,carré+1):
            if a**2+b**2==c**2:
               if a+b+c==n:
                  nbr=a*c*b
                  liste.add(nbr)
               
   return liste
            

for i in range(480,1000):
   if i%10 ==0:
      print(i)
   nbr = len(nbrsolution(i))
   if nbr > lpg:
      lpg=nbr
      print(lpg," ",nbrsolution(i)," ",i)
#int(math.sqrt(n))+1
#max. 810
# 6, 720
