a=0
for i in range(10,100):
   newn=0.1
   newd=0.1
   for j in range(10,100):
      if i/j >= 1:
         a+=1
      else :
         for k in range(3):
            b= str(i)
            chiffren=b[k-1]
            for l in range(3):
               c=str(j)
               chiffred=c[l-1]
               if chiffren == chiffred:
                  if k == 1:
                     newn=b[1]
                  if k == 2:
                     newn=b[0]
                  if l == 1:
                     newd=c[1]
                  if l == 2:
                     newd=c[0]
                  if b[-1]==0 or int(newn)== 0:
                     a+=1
                  else:
                     if c[-1]==0 or int(newd) ==0:
                        a+=1
                     else:
                        if i/j == int(newn)/int(newd) :
                           print(i,"/",j," ",newn,"/",newd)
#26/65 = 2/5
#16/64 = 1/4
#19/95 = 1/5
#49/98 = 4/8
                           
                           
            
         
      
