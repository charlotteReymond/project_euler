#euler 40
concatenating="0."
for i in range(1,500000):
   concatenating += str(i)

j=1
somme=1
print("finish")

while j < 10000000:
   print(j)
   somme*=int(concatenating[j+1])
   j=j*10
print(somme)
