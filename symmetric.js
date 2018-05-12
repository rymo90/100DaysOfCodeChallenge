function sym(arg) {
  var temp = []
  for (var k = 0; k < arguments.length; k++) {
    temp.push(arguments[k]);
  }

  function twosym(arr1, arr2) {
    var newArr = [];
    arr1.forEach(function(i) {
      if (arr2.indexOf(i) < 0 && newArr.indexOf(i) < 0) {
        newArr.push(i);
      }
    });
    arr2.forEach(function(j) {
      if (arr1.indexOf(j) < 0 && newArr.indexOf(j) < 0) {
        newArr.push(j)
      }
    });
    return newArr
  }
  return temp.reduce(twosym);
}
sym([1, 2, 5], [2, 3, 5], [3, 4, 5])
