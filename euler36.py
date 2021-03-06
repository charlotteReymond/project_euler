somme=0
for i in range(1000000) :
   n=str(i)
   bi=bin(i)[2:]
   
   if n == "".join(reversed(n)):
      if bi == "".join(reversed(bi)):
         
         somme+=i

print("somme = ",somme)
