#euler 41
import itertools
lpg=1
perm=[]
def isPrime(n): # return True if n is prime
   m = int(n)
   if m==1 or m == 0:
      return(False)
   for i in range(2, m):
      if m%i==0 :
         return(False)
         break
   return(True)
def preperm(n):
   preperm=str(1)
   for i in range(2,n+1):
      preperm+=(str(i))
   return(preperm)
   
for n in range(1,10):  
   perm+=list(itertools.permutations(preperm(n),n))

#print(perm)
for i in perm:
   perm3=''
   perm3+=str(''.join(map(str,i)))
   if isPrime(int(perm3))==True:
      if int(perm3) > lpg :
         print(perm3)
         lpg=int(perm3)
