//   17

uni = [0,3,3,5,4,4,3,5,5,4]
diz = [0,0,6,6,5,5,5,7,6,6]
cen = [0,13,13,15,14,14,13,15,15,14]


somme = 0

for(x=0;x<1000;x++){
  nombre = String(x)
  if(nombre.length == 2){
    dizaine=parseInt(nombre[0],10)
    somme=somme+diz[dizaine]
    unitee=parseInt(nombre[1],10)
    somme=somme+uni[unitee]
    console.log(nombre + '  '+somme)
  }
  else if (nombre.length==1) {
    unitee=parseInt(nombre[0],10)
    somme=somme+uni[unitee]
    console.log(nombre+'  '+somme)
  }
  else{
    centaine=parseInt(nombre[0],10)
    somme=somme+cen[centaine]
    dizaine=parseInt(nombre[1],10)
    somme=somme+diz[dizaine]
    unitee=parseInt(nombre[2],10)
    somme=somme+uni[unitee]
    if(nombre%100==0){
      somme=somme-3
    }
    console.log(nombre + '  '+somme)
  }

}
//somme=somme+11//one thousand
/*somme=somme+3//one
somme=somme+3
somme=somme+5
somme=somme+4
somme=somme+4
somme=somme+3
somme=somme+5
somme=somme+5
somme=somme+4
somme=somme+3//ten
somme=somme+6
somme=somme+6//twelve
somme=somme+8
somme=somme+8//fourteen
somme=somme+7
somme=somme+7//sixteen
somme=somme+9
somme=somme+8
somme=somme+8//nineteen*/


console.log('resultat =  '+somme)
