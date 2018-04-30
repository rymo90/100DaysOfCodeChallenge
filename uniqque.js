function uniqarr(arr){
  const result = [];
  const newArr = Array.prototype.concat(...arguments);
  for (var i = 0; i < newArr.length; i++) {
    if (!(newArr[i] in result)) {
      result.push(newArr[i])
    }
  }
  return result
}
uniqarr([1, 2, 3], [5, 2, 1, 4], [2, 1], [6, 7, 8]);
// console.log(svar);
