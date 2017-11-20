function LoadInfo() {
  var date = document.forms["infoForm"]["date"].value;
  var Attendance = document.forms["infoForm"]["attendance"].value;
  var Males = document.forms["infoForm"]["slider"].value;
  var Females = 100- document.forms["infoForm"]["sldier"].value;
  params = 'date='+date+'&attendance='+Attendance+'&Males='+Males+'&Females='+Females;
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
