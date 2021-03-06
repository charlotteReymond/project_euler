#euler29

result= {str(16)}
for a in range(2,101):
   for b in range(2,101):
      x=str(a**b)
      result.add(x)
print(len(result))
