# euler 45

def pentagone(n) :
   x=n*(3*n-1)/2
   return(x)
def hexagone(n) :
   x=n*((2*n)-1)
   return(x)




for j in range(100000) :
   nbrpenta = pentagone(j)
   for k in range(100000) :
      nbrhexa = hexagone(k)
      if nbrpenta==nbrhexa:
            print(nbrpenta,"=",nbrhexa)


1533776805
