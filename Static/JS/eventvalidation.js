function formEventValidate() {
  console.log("hello");
  var date=document.getElementById("date").value;
  var attendance=document.getElementById("Attendance").value;
  var eventType=document.getElementById("eventType").value;
  var ageRange=document.getElementById("AgeRange").value;

  if(date == null || Attendance==null || eventType==null || AgeRange ==null)
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
  var Attendance = document.forms["infoForm"]["attendance"].value;
  var Males = document.forms["infoForm"]["slider"].value;
  var Females = 100- document.forms["infoForm"]["sldier"].value;
  var Events = document.forms["infoForm"]["eventType"].value;
  var age = document.form["infoForm"]["age"].value;
  params = 'date='+date+'&attendance='+Attendance+'&Males='+Males+'&Females='+Females+'&Events='+Events+'&age='+age;
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
unsure still of how to approach age range since multiple can be added - duplicates etc//
unsure of how to validate time, so not in the past.//
