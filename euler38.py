#euler 38
tout=''
lpg=0
def pandigital(n):
   a=0
   string=str(n)
   for i in range(1,10):
      string2=str(i)
      if string2 in string:
         a+=1
   if a == 9:
      return(True)
   else:
      return(False)



a=0
for i in range(10000):
   if i%1000 == 0:
      print(i)
   tout=''
   for j in range(1,10):
      nombre=i*j
      tout += str(nombre)
      if len(str(tout)) > 9:
         a+=1
      else:
         if pandigital(tout)== True:
            tout2=int(tout)
            if tout2>int(lpg):
               lpg=tout
               print(lpg)
print('result ',lpg)
