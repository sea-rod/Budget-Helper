function change(i) {
    window.location = '/'+i+'/category_info/';
}

function cat_info_add() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        document.getElementById("content").innerHTML =
        this.responseText;
  }
  xhttp.open("GET", "/info/add");
  xhttp.send();
}