#euler 49
def isPrime(n):
   for i in range(2, int(n)-1):
      if n % i == 0:
         return(False)
   if n>1 :
      return(True)
   else:
      return(False)
import itertools

for i in range(1480,10000):
   perm=[]
   permu=[]
   if isPrime(i)  == True:
      j = i+3330
      stri=str(i)
      if isPrime(j)==True:
         strj=str(j)
         k=j+3330
         if isPrime(k)==True:
            strk=str(k)
            perm=list(itertools.permutations(stri,4))
            for a in perm:
               perm3=''
               permu.append(str(''.join(map(str,a))))
               if permu.count(strj) != 0:
                  if permu.count(strk) !=0:
                     print(a)
