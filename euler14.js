//   14
somme=1 // longueur chaîne
n=10
i=10
grandNombre=0
while(i<1000000){
n=i
    //  console.log(n)
  for(;n>1; ){


      if(n%2==0){
          n=n/2
          somme=somme+1
            }
      else {
          n=n*3+1
          somme=somme+1
        }

  }
  if(somme>grandNombre) {
    grandNombre=somme
    console.log(i)
  }
i++;
somme=1
}
