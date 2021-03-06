//   21
somme1=0
somme2=0
n=0
for(i=0;i<10000;i++){
  while(n<i){
    if(i%n==0){
      somme1=somme1+n
//console.log(n +'  '+somme1)
    }
    n++
  }
//console.log(i +'  '+somme1)
  n=1
  while(n<somme1){
    if(somme1%n==0){
      somme2=somme2+n
    }
    if(i==somme2 && somme1!=i){
      console.log(somme1+'  '+somme2)
    }
    n++
}
  n=0
  somme1=0
  somme2=0

}
