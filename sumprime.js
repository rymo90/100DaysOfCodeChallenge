function isPrime(value) {
  var isprime=[];
  var result = 0;
  var prime= [];
  for(var i = 2; i <= value; i++) {
    if (!isprime[i]) {
      prime.push(i);
      for(var j = i<<1; j<=value; j+=i){
        isprime[j]= true;
      }
    }
  }
  for(var k = 0; k < prime.length;k++){
    result += prime[k];
  }
  return result;

}
// test here
sx = isPrime(977);
console.log(sx);
