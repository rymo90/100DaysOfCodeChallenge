function dropit(arr,func) {
  var result = [];
  for(var i = 0; i< arr.length; i++){
    var test= func(arr[i]);
    if (test) {
      result= arr.slice(i);
      return result;
      break;
    }else {
      continue;
    }
  }

}
var result = dropit([1, 2, 3, 7, 4],function (n) {
  return n >5;
});
console.log(result);
