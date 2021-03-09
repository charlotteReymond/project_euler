#euler 32
def pandigital(n,x): # return True if n is a pandigital number of x
   a=0
   string=str(n)
   for i in range(1,x+1):
      string2=str(i)
      if string2 in string:
         a+=1
   if a == x:
      return(True)
   else:
      return(False)
sommeT=0
pand={0}
for i in range(10000):
   if i % 100==0:
      print(i)
   for j in range(10000):
      somme=i*j
      string=str(somme)+str(i)+str(j)
      if len(string)==9:
         if pandigital(string,9):
            pand.add(somme)

for a in pand:
   sommeT+=int(a)

print(sommeT)
