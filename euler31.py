#euler coins sum
coins = [200, 100, 50, 20, 10, 5, 2, 1]

somme = 0
result = 0
for j in range(100) :
   for i in range(len(coins)) :
      nbr = somme =+ coins[i]
      if nbr == 200 :
         result+=1
         print(coins[i] , " ",result)
   somme = 0
   nbr=0

         
