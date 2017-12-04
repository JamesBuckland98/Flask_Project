function myEventFunction() {
  var activity = document.getElementById("game");
  var select = document.createElement("select");
  var option0 = document.createElement("option");
  var option1 = document.createElement("option");
  var option2 = document.createElement("option");
  var option3 = document.createElement("option");
  option0.text = "-- select a game type --";
  option1.text = "Tag";
  option2.text = "Touch";
  option3.text = "Contact";
  option1.value = "Tag"
  option2.value = "Touch"
  option3.value = "Contact"
  activity.append(select)
  select.add(option0)
  select.add(option1)
  select.add(option2)
  select.add(option3)
  option0.setAttribute("disabled", false);
}
function myEventFunction2(){
  var element = document.getElementById("game");
  element.removeChild(element.lastElementChild);
  element.removeChild(element.lastElementChild);
  element.removeChild(element.lastElementChild);
}
function myAgeFunction() {
  var AgeGroup = document.getElementById("game");
  var br = document.createElement("br");
  var select = document.createElement("select");
  var option0 = document.createElement("option")
  var option1 = document.createElement("option");
  var option2 = document.createElement("option");
  var option3 = document.createElement("option");
  option0.text = "-- select an age range --";
  option1.text = "Minis (4-7)";
  option2.text = "Juniours (8-17)";
  option3.text = "Seniors (18+)";
  option1.value ="Minis"
  option2.value ="Juniours"
  option3.value ="Seniors"
  AgeGroup.append(select)
  select.add(option0)
  select.add(option1)
  select.add(option2)
  select.add(option3)
  AgeGroup.append(br);
  option0.setAttribute("disabled", false);
}
