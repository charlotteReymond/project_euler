# euler30
somme = 0
sommetotale = 0
for i in range(1000000) :

   nombre = str(i)
   longueure = len(nombre)
   a=0
   while a < longueure :
      b = int (nombre[a-1])
      somme=somme+b**5
      a +=1
   #print("nombre :",i," somme : ",somme)
   if i == somme :
      print(i)
      sommetotale += i
   somme=0
sommetotale -=1
print("result = ",sommetotale)
