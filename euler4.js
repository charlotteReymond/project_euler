// 4

for(a=999;a>0;a--){
	for(b=0;b<1000;b++){
		n=a*b
		//console.log(n)
		chaine = n.toString()
		longueur=chaine.length
		//console.log('n='+n+' , L:'+longueur)
		inverse = chaine[longueur-1]+chaine[longueur-2]+chaine[longueur-3]+chaine[longueur-4]+chaine[longueur-5]+chaine[longueur-6]

	//	console.log('inverse='+inverse)
		if (inverse == chaine) {
			console.log('palyndrome ='+chaine +'='+a +'*'+b)

		}
	}

}






/*
console.log(chaine[1])



for (i=longueur-1;i<0;i--){
	plouf(i)
	console.log(i);
}
*/
