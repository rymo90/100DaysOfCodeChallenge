function sumAll(arr) {
  var max_num = Math.max(...arr);
  var min_num = Math.min(...arr);
  var arra = [];
  for(var i = min_num; i <= max_num;i++){
    arra.push(i);
  }
  var sum= arra.reduce(function(a,b){
    return a + b;
  }, 0);
  return sum;
}

sumAll([1, 4]);
