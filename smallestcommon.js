//noprotect
function smallcommon(arr) {
  var start= Math.min(arr[0],arr[1]),
      end= Math.max(arr[0],arr[1]),
      arrRange = [];
  for (var i = start; i <= end; i++) {
    arrRange.push(i);
  }
  var LCM= 0,
      found= true;
  while (found) {
    LCM++;
    for(var j = start ;j <= end; j++){
      if (LCM%j!==0) {
        break;
      }else if (j===end) {
        found= false;

      }
    }

  }
  return LCM;

}
svar= smallcommon([1,5])
console.log(svar);
