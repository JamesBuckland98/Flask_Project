var slider = document.getElementById("myRange");
var Females = document.getElementById("Women");
var Males = document.getElementById("Men");
Females.innerHTML = slider.value;
Males.innerHTML = slider.value;
slider.oninput = function() {
  Females.innerHTML = 100 - this.value;
  Males.innerHTML = this.value;
}
