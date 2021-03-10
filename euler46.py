#euler 46

def isPrime(n): # return True if n is prime
   m = int(n)
   if m==1 or m == 0:
      return(False)
   for i in range(2, m):
      if m%i==0 :
         return(False)
         break
   return(True)
oddC=[]
prime=[]
for i in range(999,10000):
   if i % 2==1:
      if isPrime(i)==False:
         oddC.append(i)
for j in range(2,10000):
   if isPrime(j)==True:
      prime.append(j)

for n in oddC:
   somme=0
   print(n)
   for a in range(int(n/2)):
      for b in prime:
         if b < n:
            if b+2*a**2==n:
               somme+=1
   if somme==0:
      print("result =",n)
         
   
