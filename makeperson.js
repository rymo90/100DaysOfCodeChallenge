var Person = function(firstAndLast) {
  var temp = firstAndLast.split(' ')
  this.setFirstName = function (first){
    if (first=== undefined) {
      this.firstName= temp[0]
    }else {
      this.firstName= first;
    }
    console.log(this.firstName);
  }
  this.getFirstName = function(){
    return this.setFirstName();
  }
  this.setLastName= function(last){
    if (last===undefined) {
      this.lastName= temp[1]
    }else {
      this.lastName= last;
    }
    console.log(lastName);
  }
  this.getLastName = function(){
    return this.lastName;
  }
  this.setFullName= function(fullName){
    this.firstAndLast= fullName;
  }
  this.getFullName = function() {
    return this.firstAndLast;
  };
};

var bob = new Person("Bob mury");
// bob.getFullName();
// bob.setFirstName("Redwan")
bob.getFirstName()
// bob.setLastName("yassin")
// bob.getLastName()
// // bob.setFullName("Redwan yassin mohammedberhan")
// bob.getFullName()
// console.log(Object.keys(bob).length);
// console.log(bob.firstName());
