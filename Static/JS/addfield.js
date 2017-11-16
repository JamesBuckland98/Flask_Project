function myEventFunction() {
  var activity = document.getElementById("activity");
  var br = document.createElement("br");
  var select = document.createElement("select");
  var option0 = document.createElement("option");
  var option1 = document.createElement("option");
  var option2 = document.createElement("option");
  var option3 = document.createElement("option");
  option0.text = "-- select an option --";
  option1.text = "Tag";
  option2.text = "Touch";
  option3.text = "Contact";
  activity.append(select)
  select.add(option0)
  select.add(option1)
  select.add(option2)
  select.add(option3)
  activity.append(br);
}
function myEventFunction2(){
  var element = document.getElementById("activity");
  element.removeChild(element.lastElementChild);
  element.removeChild(element.lastElementChild);
}
function myAgeFunction() {
  var AgeGroup = document.getElementById("AgeRange");
  var br = document.createElement("br");
  var select = document.createElement("select");
  var option0 = document.createElement("option");
  var option1 = document.createElement("option");
  var option2 = document.createElement("option");
  var option3 = document.createElement("option");
  option0.text = "-- select an option --";
  option1.text = "Minis (4-7)";
  option2.text = "Juniours (8-17)";
  option3.text = "Seniors (18+)";
  AgeGroup.append(select)
  select.add(option0)
  select.add(option1)
  select.add(option2)
  select.add(option3)
  AgeGroup.append(br);
}
function myAgeFunction2(){
  var element = document.getElementById("AgeRange");
  element.removeChild(element.lastElementChild);
  element.removeChild(element.lastElementChild);
}
