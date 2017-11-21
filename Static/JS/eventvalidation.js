function formEventValidate(){
  var date=document.getElementById("date").value;
  var attendance=document.getElementById("Attendance").value;
  var eventType=document.getElementById("eventType").value;
  var ageRange=document.getElementById("AgeRange").value;

  if(date == "mm/dd/yy" || Attendance=="" || eventType=="-- select an option --" || AgeRange ="-- select an option --")
  {
    alert("All fields must be completed.")
    return false;
  }
else if(isNan(attendance));
{
  alert(attendance + "is not a valid NUMBER of attendees.")
  return false;
}
else{
  alert("Event submitted successfully")
  return true;
}
}
//unsure still of how to approach age range since multiple can be added - duplicates etc//
//unsure of how to validate time, so not in the past.//
