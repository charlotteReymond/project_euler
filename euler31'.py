#euler 31 coins sum
somme=0
sommeTotale=0
a=0
for i in range(2):
   somme+=200
   if somme == 200 :
      sommeTotale +=1
      print(sommeTotale)
   if somme > 200 :
               somme = 0
   for j in range(3):
      somme+=100
      if somme == 200:
         sommeTotale +=1
         print(sommeTotale)
      if somme > 200 :
         somme = 0
               
      for k in range(5):
         somme+=50
         if somme==200:
            sommeTotale +=1
            print(sommeTotale)
         if somme > 200 :
               somme = 0
         for l in range(11):
            somme+=20
            if somme == 200:
               sommeTotale +=1
            if somme > 200 :
               somme = 0
            for m in range(21):
               somme+=10
               if somme == 200:
                  sommeTotale +=1
                  print(sommeTotale)
               if somme > 200 :
                  somme = 0
                  for n in range(41):
                     somme+=5
                     if somme == 200:
                        sommeTotale +=1
                        print(sommeTotale)
                     if somme > 200 :
                        somme = 0
                     for o in range(101):
                        somme+=2
                        if somme == 200:
                           sommeTotale +=1
                           print(sommeTotale)
                        if somme > 200 :
                           somme = 0
                        for p in range(201):
                           somme+=1
                           if somme == 200:
                              sommeTotale +=1
                              print(sommeTotale)
                           if somme > 200 :
                              somme = 0
                                 
                              
print(sommeTotale," ",somme)
            
