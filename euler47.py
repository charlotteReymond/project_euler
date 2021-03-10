#euler 47
def primeFactors(n):
    prime = set()
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            prime.add(d)
            n //= d
        d += 1
    if n > 1:
       prime.add(n)
    return prime

somme=0
for i in range(100,1000000):
   if len(primeFactors(i))==4:
      somme+=1

      if somme == 4:
         print(i)
   if len(primeFactors(i))!=4:
      somme=0
   
