
function orbitalPeriod(arr) {
  var GM = 398600.4418;
  var earthRadius = 6367.4447;
  var temp;
  var lis = []
  var result = arr.forEach(function(i){
    temp = (2*Math.PI*Math.sqrt(Math.pow(i.avgAlt+earthRadius,3)/GM));
    lis.push({
      name: i.name,
      orbitalPeriod: Math.round(temp)
    });
  });
  console.log(lis);

}

orbitalPeriod([{name: "iss", avgAlt: 413.6}, {name: "hubble", avgAlt: 556.7}, {name: "moon", avgAlt: 378632.553}])
