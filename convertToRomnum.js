function convertToRoman(num) {
  var rum = "";
  var temp= 0;
  if(num.length == 4){
    arr4 = ["M","V","V⁻"];
    temp = num[0];
    if(temp < 5){
      if(temp==4){
        rum+=arr4[0]+arr4[1];
      }else{
        while (temp >0){
          rum+= arr4[0];
          temp -= 1;
        }
        return rum;
      }
    }else{
      if(temp == 9){
        rum+= arr4[0]+arr4[2];
      }else if(temp== 5){
        rum += arr4[1];
      }else{
        rum += arr4[1];
        while (temp > 5){
          rum+= arr4[0];
          temp -= 1;
        }
      }
    }
  }
 

}

convertToRoman(3000);
