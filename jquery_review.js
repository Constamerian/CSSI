/*function setup () {
  $("body").append("<div></div>");
  $("div").mouseenter(changeColorToBlue);
  $("div").mouseleave(changeColorToRed);
}

function changeColorToBlue () {
  $(this).removeClass("red");
  $(this).addClass("blue");
  $(this).text("blue");
//this refers to target of our event so in this case = "div"
}

function changeColorToRed () {
  $(this).removeClass("blue");
  $(this).addClass("red");
  $(this).text("red");
}

$(document).ready(setup);*/

function greeting() {
  var userName = $('#username').val();
  var header = $("h2");
  header = header.text("Hello, " + userName + "!");
}

function setup() {
  $("#ok_button").click(greeting);
  $("#hobbies").keypress(function(e){
    if (e.keyCode == 13) {
      e.preventDefault();
      var hobbies = $("#hobbies").val();
      var list = $("h3");
      list = list.append(hobbies + "<br>");
      $("#hobbies").val("");
    }
  });
  $("body").click(changeBackgroundColor);
}

function changeBackgroundColor() {
  $("body").css("background-color","green");
}

$(document).ready(setup);
