// euler24

permutations=[]
somme=0
for(a=0;a<10;a++){
  for(b=0;b<10;b++){
    for(c=0;c<10;c++){
      for(d=0;d<10;d++){
        for(e=0;e<10;e++){
          for(f=0;f<10;f++){
            for(g=0;g<10;g++){
              for(h=0;h<10;h++){
                for(i=0;i<10;i++){
                  for(j=0;j<10;j++){

      aa = new String (a)
      bb = new String (b)
      cc = new String (c)
      dd = new String (d)
      ee = new String (e)
      ff = new String (f)
      gg = new String (g)
      hh = new String (h)
      ii = new String (i)
      jj = new String (j)


      permutation= new String (aa+bb+cc+dd+ee+ff+gg+hh+ii+jj)

    if(a!=b && a!=c && a!=d && a!=e && a!=f && a!=g && a!=h && a!=i && a!=j){
      if(b!=c && b!=d && b!=e && b!=f && b!=g && b!=h && b!=i && b!=j){
        if(c!=d && c!=e && c!=f && c!=g && c!=h && c!=i && c!=j){
          if(d!=e && d!=f && d!=g && d!=h && d!=i && d!=j ){
            if(e!=f && e!=g && e!=h && e!=i && e!=j){
              if(f!=g && f!=h && f!=j && f!=i ){
                if(g!=h && g!=i && g!=j){
                  if(h!=i && h!=j){
                    if(i!=j){
                      console.log(permutation)
                      permutations.push(permutation)
                      somme=somme+1
                      if(somme==1000000){
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')
                        console.log('fini')


                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
}
}
}
}
}
}
}
}
}
}
