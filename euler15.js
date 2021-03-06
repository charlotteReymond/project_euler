//     15
function Fact(nbr) {
  fact = 1
  for(i=1;i<=nbr;i++){
    fact=fact*i
  }
  return fact;
}

n= Fact(40)
k= Fact(20)
h= Fact(20)

solution=n/(k*h)
console.log(solution  + '   '+n)

//solution = 137846528820
