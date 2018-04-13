function dnapair(kn) {
  var str = kn.split("");
  arr = []
  str.forEach(function(i){
    if (i == "A") {
      arr.push([i,"T"]);
    }else if (i == "T") {
      arr.push([i,"A"]);
    }else if (i=="C") {
      arr.push([i,"G"]);
    }else if (i=="G") {
      arr.push([i,"C"]);
    }
  });
  return arr
}
dnapair("CTCTA")
