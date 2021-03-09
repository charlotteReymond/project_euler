//  9
for (c=1; c<1000; c++){
for (a= 1; a < 1000; a++) {
  for(b=1;b<1000;b++){
    aa=a*a
    bb=b*b
    cc=c*c
    if(cc==aa+bb) {
      if(c+a+b==1000){
      console.log(a + '  '+ b +'  ' + c)
    }
  }
  }
}
}
