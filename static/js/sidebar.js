const links = document.querySelectorAll("#sidebar a");
console.log("kk");

links.forEach((element) => {
  if (element.href === window.location.href) {
    element.classList.add("active");
  } else {
    element.classList.remove("active");
  }
});
