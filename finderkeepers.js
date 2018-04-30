function finderkeeper(arr,func) {
  var result;
  for(var i = 0; i < arr.length;i++){
    var tes = func(arr[i]);
    // console.log(tes);
    if (tes) {
      result= arr[i];
      break

    }
  }
  return result;
}
var res= finderkeeper([1, 3, 5, 9],function(num){return num%2===0;});
console.log(res);
