function binaryAgent(str) {
  var word = "";
  var result = "";
  var num = 0;
  // result
  for (var k in str) {
    var i = 0;
    if (str[k] !== " ") {
      word += str[k];
    } else {
      num = parseInt(word, 2);
      result += String.fromCharCode(num);
      word = "";
    }
  }
  if (word == "00111111") {
    result += "?";
  } else {
    result += "!";
  }
  console.log(result);
}
binaryAgent("01000001 01110010 01100101 01101110 00100111 01110100 00100000 01100010 01101111 01101110 01100110 01101001 01110010 01100101 01110011 00100000 01100110 01110101 01101110 00100001 00111111");
