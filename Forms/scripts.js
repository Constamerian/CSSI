function greeting() {
  var userName = $('#username').val();
  alert("Hi " + userName + ",\nYou is kind\nYou is smart\nYou is important");
  var header = $("h2");
  header = header.text(userName + " is cool");
}

function setup() {
  $("#ok_button").click(greeting);
}

//function changeHeader(user) {
//  var header = $("h2");
//  header.text(user + " Hi");
//}

$(document).ready(setup);
