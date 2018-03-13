function convertToRom(num){
    num = num.toString();  
    var lng = num.length;
    while(lng >= 1){
        var rum = "";
        var temp = num[0];
        var obj = {
            "1": ["I","V","X"],
            "2": ["X","L","C"],
            "3": ["C","D","M"],
            "4": ["M","V","X⁻"]
        };
        if(obj[lng]){
            if(temp < 5){
                if(temp==4){
                  rum+=obj[lng][0]+obj[lng][1];
                }else{
                  while (temp >0){
                    rum+= obj[lng][0];
                    temp -= 1;
                  }
                }
              }else{
                if(temp == 9){
                  rum+= obj[lng][0]+obj[lng][2];
                }else if(temp== 5){
                  rum += obj[lng][1];
                }else{
                  rum += obj[lng][1];
                  while (temp > 5){
                    rum+= obj[lng][0];
                    temp -= 1;
                  }
                }
              }
        }else{
            continue;
        }
        
        return rum + convertToRom(num.substr(1,num.length))
    }
    return ""
}
var result = convertToRom(343);
console.log(result);
