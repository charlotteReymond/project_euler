//,,,18
somme=0
var l1=[75]
var l2=[95,64]
var l3=[17,47,82]
var l4=[18,35,87,10]
var l5=[20,04,82,47,65]
var l6=[19,01,23,75,03,34]
var l7=[88,02,77,73,07,63,67]
var l8=[99,65,04,28,06,16,70,92]
var l9=[41,41,26,56,83,40,80,70,33]
var l10=[41,48,72,33,47,32,37,16,94,29]
var l11=[53,71,44,65,25,43,91,52,97,51,14]
var l12=[70,11,33,28,77,73,17,78,39,68,17,57]
var l13=[91,71,52,38,17,14,91,43,58,50,27,29,48]
var l14=[63,66,04,68,89,53,67,30,73,16,69,87,40,31]
var l15=[04,62,98,27,23,09,70,98,73,93,38,53,60,04,23]

var lignes = [l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14,l15]
for(l=14;l>=0;l--){
  console.log('on est a la ligne '+l)
  for(x=0;x<13;x++){
    ligne=lignes[l]
    lig=lignes[l-1]
    if(ligne[x]>ligne[x+1]){
      nombre=lig[x]+ligne[x]
      console.log(lig[x] + '  +  '+ligne[x]+'  =  '+ nombre )
      lig[x]=nombre
    }
    else{
      nombre=lig[x]+ligne[x+1]
      console.log(lig[x] + '  +  '+ligne[x+1]+'  =  '+ nombre )
      lig[x]=nombre
  }
}
}
