function unFlip(n) {
  var detail = document.getElementById(n);

  if (detail.style.display == "none") {
      detail.style.display = "inline";
  } else {
      detail.style.display = "none";
  }
}

