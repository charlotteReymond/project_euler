//   19
somme=0
compte=5
var jourMois = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
var nomMois = ['janvier','fevrier','mars','avril','mai','juin', 'juillet','aout','septembre','octobre','novembre','decembre']
var jourAnnee = 365
var jourSemanine =['lundi', 'mardi','mercredi','jeudi','vendredi','samedi','dimanche']
for(year=1901;year<2001;year++){
  //sconsole.log('l annee est '+year)
  if((year-1)%4 == 0 && year!= 2000){
    jourMois[1]=29
  }

  for(month=0;month<12;month++){
    compte=compte+jourMois[month]
    if(compte%7==0){
      somme = somme+1
      console.log('le mois de ' + nomMois[month] +'.'+year+'    la somme est de ' +somme)
    }
    jourMois[1]=28
  }
}
//01.01.1906
