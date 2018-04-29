function addTogether() {
  function checknum(num) {
    return typeof num === "number"? num : undefined;
  }
  firstarg= checknum(arguments[0]);
  secondarg= checknum(arguments[1]);
  if (arguments.length > 1) {
    return firstarg&&secondarg? firstarg+secondarg:undefined;
  }else {
    if (firstarg) {
      return function(y){
        if (checknum(y)) {
          return firstarg+y
        }else {
          return undefined;
        }
      }
    }else {
      return undefined;
    }
  }


}
var svar= addTogether(2);
console.log(svar);
