// 12
somme=0
nbrDiviseur=0
for(a=1;a<=100000;a++){
  somme=somme+a
console.log('  .  ')
  for(i=1;i<1000000;i++){
    if(somme%i == 0){
      nbrDiviseur=nbrDiviseur+1
        if(nbrDiviseur == 500 ){
          console.log(somme+'   '+nbrDiviseur)
        }
    }
  }
  nbrDiviseur=0
}




//  solution  == 76576500 
