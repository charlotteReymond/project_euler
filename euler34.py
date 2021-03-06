#euler 34 (digits fatorial)
factorial(nbr) :
    fact = 1
    i=1
        while (i<=nbr){
        fact=fact*i
        i++
    return(fact)

sum=0
for i in range(150):
    n=str(i)
    for j in range(len(i)):
        sum+=factorial(n[j])
    print(n," -> ",sum)
