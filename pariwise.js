function pairwise(arr,arg) {
  var svar=0
  for(var i = 0; i < arr.length;i++){
    for(var k = i+1; k < arr.length-1; k++){
      if (arr[i]+arr[k]===arg) {
        svar += i+k

      }
    }
  }
  console.log(svar);
}
pairwise([1, 4, 2, 3, 0, 5], 7);
