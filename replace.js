function reaplacewor(txt,byt,ny) {
  var temp = txt.split(" ")
  console.log(temp);
  firsupper= /[A-Z]/.test(byt[0]);
  for(var i= 0; i< temp.length; i++){
    if (temp[i]===byt ) {
      if (firsupper) {
        temp.splice(i,1,ny.charAt(0).toUpperCase()+ny.slice(1));

      }else{
        temp.splice(i,1,ny);

      }
    }

  }
  console.log(temp);
  // console.log(lis.splice(ten,1,ny));
  console.log(temp.join().replace(/,/gi,' '));
}
reaplacewor("Let us go to the store", "store","mall")
