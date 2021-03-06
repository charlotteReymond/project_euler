# euler 25

a=1
b=1
somme=2
for i in range(130000):
   c=a+b
   a=b
   b=c
   somme +=1
   if len(str(c)) == 1000:
      print(somme)
