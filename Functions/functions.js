function timesTwo (number) {
  var value = number*2;
  return value;
}

function timesSix (number) {
  var result = timesTwo (number);
  result = result*3;
  return result;
  /* or just return timesTwo(number)*3 */
}

function rollDice () {
  return Math.floor((Math.random() * 6) + 1);
}

function finalCost (price, tax) {
  var salesTax = price + price*.095;
  var modifiedsalesTax = salesTax*100;
  modifiedsalesTax = Math.round(modifiedsalesTax);
  return modifiedsalesTax/100;
}

function totalCost (bill, tax, tip) {
  var billandTax = bill + bill*taxpercentageindecimal;
  var billtaxtip = billandTax*tippercentageindecimal;
  billtaxtip = Math.round(billtaxtipp*100);
  return billtaxtip/100;
}

//function arrayDoubled(orginalArray) {
//  var originalArray = [1, 2, 3, 4];
//  for(var i = 0; i < originalArray.length; i++) {
//    var number = originalArray[i]*2;
//    alert(number);
//  }
//}

//function reverseArray(originalArray) {
  //var originalArray = [1, 2, 3, 4, 5, 6];
  //var length = originalArray.length;
  //var newArray = [];
  //for(var i = 0; i < length; i++){
    //newArray.push(originalArray.pop(i));
  //}
  //return newArray;
//}

function mergeArray(originalArray) {
  var numbers = [1, 2, 3];
  var letters = ['a', 'b', 'c', 'd', 'e'];
  var numbersandletters = [];
  var longestlength = Math.max(letters.length, numbers.length)
  for(var i = 0; i < longestlength; i++) {
    if(numbers[i] != undefined) {
      numbersandletters.push(numbers[i])
    }
    if(letters[i] != undefined){
      numbersandletters.push(letters[i])
    }
  }
  return numbersandletters;
}

function EJLF(facts){
var johnLennonFacts = ['a', 'b', 'c'];
var excitingFacts = [];
var i = 0
while(i < johnLennonFacts.length){
  excitingFacts.push(johnLennonFacts[i] + '!!!');
  i++;
  }
  return excitingFacts;
}

function BeatlesInstruments(musicians){
  var beatles = ["John", "Ringo", "George", "Paul"];
  var instruments = ["Guitar", "Drums", "Bass", "Guitar"];
  var BeatlesandInstruments = [];
  var i = 0;
  while (i < beatles.length){
    BeatlesandInstruments.push(beatles[i] + ' played ' + instruments[i]);
    i++;
  }
  return BeatlesandInstruments;
}

//function niceRegularBox(arr){
  //var longest = arr.sort(function(a,b) {return }
//}
