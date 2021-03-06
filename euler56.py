#euler 56
lpg=0
for i in range(100):
   if i%2==0:
      print(i," ",lpg)
   for j in range(100):
      somme=0
      puissance=i**j
      for k in range(len(str(puissance))):
         puissance2=str(puissance)
         nbr=puissance2[k]
         somme+=int(nbr)
         
         if somme > lpg:
            lpg=somme
print(lpg)
