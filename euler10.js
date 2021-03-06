//  10
function isPrime(x) {
  ok=true
  i=Math.floor(Math.sqrt(x))
  while (i>1 && ok==true) {
        if(x % i == 0){
          ok=false
      }
  i--
  }
  return ok
}

somme=0
for ( a= 2; a< 2000000; a++) {
  if(isPrime(a)){
    somme=somme+a
    console.log(somme + '   ' + i)
  }
}
