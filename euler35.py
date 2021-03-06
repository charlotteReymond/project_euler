a=0
somme=49
rien=0
def isPrime(n):
   m = int(n)
   if m==1 or m == 0:
      return(False)
   for i in range(2, m):
      if m%i==0 :
         return(False)
         break
   return(True)

def rotate(strg, n):
    return strg[n:] + strg[:n]

   

for i in range(900000,1000001):
   if str(i)[0]==2 or str(i)[0]==4 or str(i)[0]==8 or str(i)[0]==6 or str(i)[0]==5 or str(i)[0]==0:
      rien+=1
   else:
      if i%1000==0:
         print(i," ",somme)
      a=0
      if isPrime(i):
         strg = str(i)
         for j in range(len(strg)):
            if isPrime(rotate(strg,j)):
               a+=1
               if a == len(strg) :
                  somme+=1
                  
                 
print(somme)
      
      

