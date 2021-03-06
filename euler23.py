#euler 23
abondant =[]
nombres=[]
abo2 = {24}
somme=0
def sommeDiviseurs(n):
   somme=0
   for i in range(1,n):
      nbr=int(n)
      if nbr%i == 0 :
         somme += i
   return(somme)

for n in range(23117):
   if sommeDiviseurs(n) > n :
      abondant.append(n)
print("abondant")

for m in range(23129):
   nombres.append(m)
print("nombres")
for i in range(len(abondant)):
   a=abondant[i]
   for j in range(len(abondant)):
      b=abondant[j]
      abo2.add(a+b)
print("abo2")

for k in range(len(abo2)):
   if k in abo2:
      if k in nombres:
         nombres.remove(k)           

for l in range(len(nombres)):
   somme+=nombres[l]

print(somme)
