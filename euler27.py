#euler 27
def isPrime(n):
   for i in range(2, int(n)-1):
      if n % i == 0:
         return(False)
   if n>1 :
      return(True)
   else:
      return(False)

print(isPrime(0))
lpg=0
for j in range(0,1000):
   if j%2==0:
      print(j,"/1000")
   for k in range(-1000,1000):
      somme=0
      for i in range(50):
         form=i**2+i*j+k
         if isPrime(form) == True:
            somme+=1
            if somme > lpg and somme==i+1:
               lpg=somme
               print(form," ",somme," =" ,i," ",j," ",k)
            

