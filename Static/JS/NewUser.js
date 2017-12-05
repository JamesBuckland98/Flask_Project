$(document).ready(function){

function ValidateNewUserForm()
{
    var FirstName = document.getElementById('FirstName').value;
    var Surname = document.getElementById('Surname').value;
    var Username = document.getElementById('username').value;
    var Email = document.getElementById('email').value;
    var contactNumber = document.getElementById('contactnumber').value;
    var Pass1 = document.getElementById('password').value;
    var Pass2 = document.getElementById('repassword').value;

    if (FirstName.value == "")
    {
        window.alert("Please enter your FirstName.");
        FirstName.focus();
        return false;
    }

    if (Surname.value == "")
    {
        window.alert("Please enter your Surname.");
        Surname.focus();
        return false;
    }

    if (username.value == "")
    {
        window.alert("Please enter your username.");
        username.focus();
        return false;
    }


    if (email.value == "")
    {
        window.alert("Please enter a valid e-mail address.");
        email.focus();
        return false;
    }
    if (email.value.indexOf("@", 0) < 0)
    {
        window.alert("Please enter a valid e-mail address.");
        email.focus();
        return false;
    }
    if (email.value.indexOf(".", 0) < 0)
    {
        window.alert("Please enter a valid e-mail address.");
        email.focus();
        return false;
    }

    if ((contactnumber.checked == false) && (contactnumber.value == ""))
    {
        window.alert("Please enter your phone number.");
        contactnumber.focus();
        return false;
    }

    if (pass1 == pass2)
    {
      alert("Passwords Match")
    }

    else
    {
      alert("Passwords Do Not Match")
    }

    return(true);

  }

});
