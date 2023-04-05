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

function cat_add() {
    const xhttp = new XMLHttpRequest();
    xhttp.onload=function(){
        document.getElementById("content").innerHTML = this.responseText;
    }
    xhttp.open('GET',"/category_add/");
    xhttp.send();
}