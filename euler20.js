//   20
function Fact(nbr) {
  nbr=100n
  fact = 1n
  i=1n
  while (i<=nbr){
    fact=fact*i
    i++
  }
  return fact;
  console.log(fact)
}
resultat=Fact()
chaine = String(resultat)
console.log(chaine)
x=0n
somme=0x
while (x<1000) {
//console.log(chaine.charAt[x])
char = parseInt(chaine[x],10)
somme=somme+char
console.log(char+'  ' +somme)
x++
}
