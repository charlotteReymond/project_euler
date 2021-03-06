def factorial(nbr):
   fact = 1
   i=1
   while (i<=nbr):
      fact=fact*i
      i+=1
   return(fact)

sum=0
sommeT=0
for i in range(1500000):
   n=str(i)
   for j in range(len(n)):
      x=int(n[j])
      sum+=factorial(x)
      if sum==i :
         print(n," -> ",sum)
         sommeT += sum
   sum=0

print("résultat = ",sommeT-3)
