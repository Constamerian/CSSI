function showWhenClicked() {
    $("#pig").show();
}

function hideWhenClicked() {
    $("#pig").hide();
}

function flyWhenClicked() {
    $("#pig").animate(
      {"margin-left": "400px"},
        4000
    );
    $("#piggy").animate(
      {"margin-left": "700px"},
        3000
    );
}

function fadeWhenClicked() {
    $("#pig").fadeOut(4000, "swing");
}

function zoomWhenClicked() {
    $("#pig").animate(
      {height: '750px',
       width: '750px'}
    )
}

function setup() {
    $("#showPig").click(showWhenClicked);
    $("#hidePig").click(hideWhenClicked);
    $("#pig").click(flyWhenClicked);
    $("#fadePig").click(fadeWhenClicked);
    $("#zoomPig").click(zoomWhenClicked);
}

$(document).ready(setup);
