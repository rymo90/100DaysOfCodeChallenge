function translatepiglating(str) {
  var lisstr = str.split("")
  var count = 0;
  if (/[aeiou]/.test(str.charAt(0))) {
    str += "way";
  } else {
    while (!/[aeiou]/.test(str.charAt(count))) {
      count += 1;
    }
    str = str.substr(count, str.length) + str.substr(0, count) + "ay";
    // console.log(str);
  }
  return str
}
sv = translatepiglating("paragraphs")
console.log(sv);
