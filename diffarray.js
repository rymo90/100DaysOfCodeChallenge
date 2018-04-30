function diffArray(arr1, arr2) {
  var newArr = [];
  arr1.forEach(function(i) {
    if (arr2.indexOf(i) < 0 && newArr.indexOf(i) < 0) {
      newArr.push(i);
    }
  });
  arr2.forEach(function(j) {
    if (arr1.indexOf(j) < 0 && newArr.indexOf(j) < 0) {
      newArr.push(j);
    }
  });
  return newArr;

}

svar = diffArray(["diorite", "andesite", "grass", "dirt", "pink wool", "dead shrub"], ["diorite", "andesite", "grass", "dirt", "dead shrub"])
console.log(svar);
