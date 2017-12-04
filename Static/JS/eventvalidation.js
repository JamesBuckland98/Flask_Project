function formEventValidate() {
  console.log("hello");
  var date=document.getElementById("date").value;
  var eventName=document.getElementById("eventName").value;
  var attendance=document.getElementById("Attendance").value;
  var eventType=document.getElementById("eventType").value;
  var gameType=document.getElementById("gameType").value;
  var ageRange=document.getElementById("AgeRange").value;

  if(date == null || eventName==null || Attendance==null || eventType==null || gameType==null || AgeRange ==null)
  {
    alert("All fields must be completed.")
    return false;
  }
else if(isNan(attendance))
{
  alert(attendance + "is not a valid NUMBER of attendees.")
  return false;
}
else{
  alert("Event submitted successfully")
  return true;
}
if (formEventValidate() == true) {
  var date = document.forms["infoForm"]["date"].value;
  var eventName = document.forms["infoForm"]["eventName"].value;
  var Attendance = document.forms["infoForm"]["attendance"].value;
  var eventType = document.forms["infoForm"]["eventType"].value;
  var Males = document.forms["infoForm"]["slider"].value;
  var Females = 100- document.forms["infoForm"]["sldier"].value;
  var gameType = document.forms["infoForm"]["gameType"].value;
  var age = document.form["infoForm"]["age"].value;
  params = 'date='+date+'&eventName'+eventName+'&attendance='+Attendance+'&eventType'+eventType+'&Males='+Males+'&Females='+Females+'&gameType='+gameType+'&age='+age;
  var xhttp = new XMLHttpRequest();
  xhttp.open("POST", '/Upload', true);
  xhttp.onload = function() {
      if (xhttp.readyState === 4 && xhttp.status === 200) {
        console.log(xhttp.responseText);
      } else {
        console.error(xhttp.statusText);
      }
    };
    xhttp.send(params);
    return false;
  }
}
// unsure still of how to approach age range since multiple can be added - duplicates etc//
// unsure of how to validate time, so not in the past.//
