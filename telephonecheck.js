function telephonecheck(str) {
  var temp = /^((1|\s|\d{10})?)+((\(\d{3}\)|\d{3})[-\s]?(\d{3}|\(\d{3}\))[-\s]?(\(\d{4}\)|\d{4}))?$/
  console.log(temp.test(str));
}
telephonecheck('555')
