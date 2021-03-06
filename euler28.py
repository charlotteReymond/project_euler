

def diago1() :
   nombre=1
   somme=0
   for i in range(1001) :
      nombre += 2*i
      somme+=nombre

      print(somme)
   return(somme)

def diago2() :
   nombre=5
   somme=0
   for i in range(1002) :
      if i%2 == 1 :
         somme += i**2
      else :
         somme += i**2 +1
      print(somme-1)  
   return(somme-2)
  
diago2()
résultat =diago1() + diago2()
print(résultat)
