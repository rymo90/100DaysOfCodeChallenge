var currency = [
  {name: 'ONE HUNDRED', value:100.00},
  {name: 'TWENTY',      value:20.00},
  {name: 'TEN',         value:10.00},
  {name: 'FIVE',        value:5.00},
  {name: 'ONE',         value:1.00},
  {name: 'QUARTER',     value:0.25},
  {name:'Dime',         value:0.10},
  {name:'NICKEL',       value:0.05},
  {name:'PENNY',        value:0.01},

];

function checkCashRegister(price, cash, cid) {
  var subt = cash - price;
  var totalCid= cid.reduce(function(acc,next){
    return acc+next[1];
  },0.0);
  if (totalCid < subt) {
    return "Insufficient Funds";
  }else if (totalCid=== subt) {
    return "Closed";
  }
  cid = cid.reverse();
  var result= currency.reduce(function(acc,next,index){
    if (subt >= next.value) {
      var currentV= 0.0;
      while (subt >= next.value && cid[index][1]>= next.value) {
        currentV += next.value;
        subt -= next.value;
        subt= Math.round(subt*100)/100;
        cid[index][1] -= next.value;
      }
      acc.push([next.name,currentV]);
      return acc;
    }else {
      return acc;
    }
  }, []);
  return result.length > 0 && subt === 0 ? result : "Insufficient Funds";
}
var res = checkCashRegister(3.26, 100.00, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.10], ["QUARTER", 4.25], ["ONE", 90.00], ["FIVE", 55.00], ["TEN", 20.00], ["TWENTY", 60.00], ["ONE HUNDRED", 100.00]])
console.log(res);
console.log("   ");
var kkk= [["TWENTY", 60.00], ["TEN", 20.00], ["FIVE", 15.00], ["ONE", 1.00], ["QUARTER", 0.50], ["DIME", 0.20], ["PENNY", 0.04]]
console.log(kkk);
