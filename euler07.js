// 7

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


myBlock:{
a=0
for (ii=2; ii<10000000000000000000000000; ii++) {

  if (isPrime(ii)) {
  a=a+1
  console.log(a+'----'+ii)
    if(a==10001){
      console.log('SOLUTUTION'+ii)
      break myBlock
    }
    }
  }
}
