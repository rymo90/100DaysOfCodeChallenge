function converthtml(str) {
  var symboler = {"&":"&amp;","<":"&lt;",">": "&gt;","'":"&apos;",'"': "&quot;"};
  for (var i = 0; i < str.length; i++) {
    if (str.charAt(i) in symboler) {
      var re = new RegExp(str.charAt(i));
      str = str.replace(re,symboler[str.charAt(i)]);
    }
  }
  return str

}
svar= converthtml("Hamburgers < Pizza < Tacos")
console.log(svar);
