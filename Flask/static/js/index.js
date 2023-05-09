// java script for form validation [by Sanjay] 

let Submit_Button = document.getElementById("Button");

function Process() {

// varaible assined for form validation 

    let User_Name = document.getElementById("username");
    let Last_Name = document.getElementById("lastname");
    let Email = document.getElementById("email");
    let Password = document.getElementById("password");
    let Languages = document.getElementById("Language");
    let Status = document.getElementById("Status");



    if (User_Name.value && Last_Name.value && Email.value && Password.value && Languages.value != "Select" && Status.value != "Select") {
        
        // assigining varibles for checking thier input if it is valid.

        let UN = false, UL = false, UE = false, UP = false;
        var Final = false;

        if (isNaN(User_Name.value)){
            UN = true;

        }
        else{
            User_Name.style.borderBottomColor = "red";
            User_Name.value = "";
        }

        if (isNaN(Last_Name.value)){
            UL = true;

        }
        else{
            Last_Name.style.borderBottomColor = "red";
            Last_Name.value = "";
        }

        if (isNaN(Email.value)){
            UE = true;

        }
        else{
            Email.style.borderBottomColor = "red";
            Email.value = "";
            UE= false;
        }

        if (Password.value.length < 7) {
            Password.value = "";
            Password.style.borderBottomColor =  "red";  
            alert("Password is too short") ;
        } 
        else {
            UP = true;
        }



        if (UN && UL && UE && UP ){
            Final = true;
        } else {

            console.log(UN , UL, UE , UP)
            alert("Please fill all field with valid imformation");

            if (UN == false) {
              User_Name.focus();
              setErrorFor(User_Name,"name is not valid")
            }
            if (UL == false) {
                Last_Name.focus();
              }
            if (UE == false) {
                Email.focus();
              }
            if (UP == false) {
                Password.focus();
              }   

        }

    } else {
        User_Name.style.borderBottomColor = "red";
        Last_Name.style.borderBottomColor = "red";
        Email.style.borderBottomColor = "red";
        Password.style.borderBottomColor = "red";
        Languages.style.borderColor = "red";
        Status.style.borderColor = "red";

        User_Name.focus()
        alert("Fill all the field Before Submit");
    }

var subjects = document.getElementsByName("topic"),
radio_Checked = null;

subjects.forEach(radio => {
    if (radio.checked) {
        radio_Checked = radio.value;
    }
});

var Final_Radio = false;

if (radio_Checked) {
    Final_Radio = true;
    
}
else{
    Final_Radio = false;
}

if(Final_Radio == false){
    alert('please select any one of radio button');

}




if(Final && Final_Radio){
    // send's final validated to server side
    form.submit()
}

}



Submit_Button.addEventListener('click',Process);

// this below code is time killing i already assigned varaible but still i wrote again


let name_input = document.getElementById("username");
let last_input = document.getElementById("lastname");
let email_input = document.getElementById("email");
let pass_input = document.getElementById("password");
let Form = document.getElementById("form");

function check_name() {
    if (isNaN(name_input.value)) {
      name_input.style.borderBottomColor = "black";
    } else {
        name_input.style.borderBottomColor = "red";

    }
}

function check_last() {
    if (isNaN(last_input.value)) {
      last_input.style.borderBottomColor = "black";
    } else {
        last_input.style.borderBottomColor = "red";

    }
}

function check_email() {
    if (isNaN(email_input.value)) {
      email_input.style.borderBottomColor = "black";
    } else {
      email_input.style.borderBottomColor = "red";

    }

    let email_data = email_input.value,
    got = false ;
    

    for(let i = 0; i < email_data.length ; i++){
        if(email_data){
            if (email_data[i] == '@') {
                got = true;

            }

        }

    }
 

    if (got) {
        email_input.style.borderBottomColor = "black";
    } else {
        email_input.style.borderBottomColor = "red";
    }


    if(email_data.includes(".com")){
        email_input.style.borderBottomColor = "black";
    }
    else{
        email_input.style.borderBottomColor = "red";
    }
}

function check_pass() {
    if (pass_input.value.length < 7) {
        pass_input.style.borderBottomColor = "red";
    } else {
        pass_input.style.borderBottomColor = "black";
    }
}

name_input.addEventListener("input",check_name);
last_input.addEventListener("input",check_last);
email_input.addEventListener("input",check_email);
pass_input.addEventListener("input",check_pass);

form.addEventListener('submit',function(event){
    event.preventDefault()
});