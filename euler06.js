// 6
somme=0
for(i=0;i<101;i++) {
  somme = somme+i
}
a=somme*somme
console.log(a)
b=0
for (var i = 0; i < 101; i++) {
  b=i*i+b
}
console.log(b)
c=a-b
console.log(c)
