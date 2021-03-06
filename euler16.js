//  16


puissance = 2n
a=2n
for(b=1;b<1000;b++){
puissance=puissance*a
}
 somme=0

console.log(puissance)
chaine = String(puissance)
x=0
while (x<1000) {
//console.log(chaine.charAt[x])
char = parseInt(chaine[x],10)
somme=somme+char
console.log(char+'  ' +somme)
x++
}
