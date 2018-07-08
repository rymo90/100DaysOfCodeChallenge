function updateInventory(arr1, arr2) {
for(var i = 0 ; i < arr2.length; i ++){
  var everyElem= arr1.every(function(element){
    return arr2[i][1]!= element[1];
  });
  if (everyElem) {
    arr1.push(arr2[i])
  }else {
    var indexfind= arr1.findIndex(function(element){
      return arr2[i][1]===element[1];
    });
    arr1[indexfind][0] +=arr2[i][0];
  }
}
var result= arr1.sort(function (a, b) {
  return a[1] < b[1]? -1: 1;
})
return result;

}
