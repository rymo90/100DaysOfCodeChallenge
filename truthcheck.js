function truthCheck(collection, pre) {
  var result= []
  var temp, lis, lastresult;
  for (var i in collection) {
    temp = collection[i];
    if (pre in temp) {
      for (var variable in temp) {
        if (variable== pre) {
          var lis = prefunction(variable,temp[variable]);
          result.push(lis)
        }
      }
    }else {
      result.push(false);
    }

  }
  function prefunction(key, value) {
    if (key == "onBoat" ) {
      if (value == true || value == false) {
        return true;
      }else {
        false;
      }
    }else if (key== "sex") {
      if (value== "male" || value == "female") {
        return true;
      }else {
        return false;
      }
    }else if (key== "age") {
      if (value > 0) {
        return true;
      }else {
        return false;
      }
    }else {
      // console.log(value);
      if (value=="yes") {
        return true;
      }else {
        return false
      }
    }
  }
  for(var i = 0; i < result.length; i++){
    if (result[i]=== false) {
      lastresult= false;
      break;
    }else {
      lastresult= true;
    }
  }
  console.log(lastresult);

}
truthCheck([{"single": "yes"}], "single");
