
somme=0
import itertools 
l=[1,2,3,4,5,6,7,8,9,0]
perm = list(itertools.permutations(l))

for i in range(len(perm)-1):
   string=perm[i]
   a1 = string[3]
   if int(a1)% 2 ==0 :
      a2 = str(string[2]))+int(string[3])+int(string[4])
      if a2 %3 ==0 :
            a3 = string[5]
            if int(a3) %5 ==0 :
               a4 = str(string[4])+str(string[5])+str(string[6])
               if int(a4) %7 ==0 :
                  a5 = str(string[5])+str(string[6])+str(string[7])
                  if int(a5) %11 ==0 :
                     a6 = str(string[6])+str(string[7])+str(string[8])
                     if int(a6) %13 ==0 :
                        a7 = str(string[7])+str(string[8])+str(string[9])
                        if int(a7) %17 ==0 :
                              somme+=i
                              print(i)

print(somme)
