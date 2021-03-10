#euler 44
penta =[]
for i in range(1,3000):
   x=(int(i*(3*i-1)/2))
   penta.append(str(x))
#print(penta)
lpp=100
for x in penta:
   for y in penta:
      if penta.count(str(int(x)+int(y)))>0:
         print(x)
         if penta.count(str(int(x)-int(y)))>0:
            print(x," ",y)
                  
