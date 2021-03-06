//  23
i=1
somme=0
abondant=[]
non =[]
sommeA=0//somme des noombres pouvant etre ecrit par 2 abondants
for(aa=0;aa<10000;aa++){
    newLength = non.unshift(aa)
}

for(n=1;n<10000;n++){
//  console.log('nombre = '+n)
  while(i<n){
    if(n%i==0){
      somme=somme+i
  //    console.log('div. '+ i+' somme '+somme)
      }
    i++
    }


  if(somme>n){
    newLength = abondant.unshift(n)
    console.log(n+' est abondant')
  }
  somme=0
  i=1
}

for(a=0;a<abondant.length;a++){
  for(b=0;b<abondant.length;b++){
    nom=abondant[a]+abondant[b]
    console.log(nom)
    pos = non.indexOf(nom)
    if(pos==-1){

    }
    else{
      removedItems = non.splice(pos,1)
      console.log(non)

    }

  }
}

for(g=0;g<non.length;g++){
  nombre=non[g]
  sommeA=sommeA+nombre
  console.log(nombre+' '+sommeA)
}
