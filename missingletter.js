function missingletter(s) {
  while (s.charAt(0)=='a') {
    var start = s.charCodeAt(0);
    for(var i = 1; i < s.length; i++){
      var sn= s.charCodeAt(i);
      if ((sn - start)== 1) {
        start = sn;
      }else{
        return String.fromCharCode(sn-1);
      }
    }
  }
  return "undefind";



}
svar= missingletter("yz")
console.log(svar);
