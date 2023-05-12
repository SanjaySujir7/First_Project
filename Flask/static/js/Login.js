
let Name_Email = document.getElementById("Name");
let Password = document.getElementById("Password");
let Button = document.getElementById("Button");
let form = document.getElementById('form');


var User_Name_Email = false , Password_valid = false , Final = true;


function Process(Data_type) {
    if (Data_type == 'Name') {
        
        if(isNaN(Name_Email.value)){
            Name_Email.style.borderColor = "gray";
            User_Name_Email = true;
            Name_Email.setCustomValidity("");
            
        }
        else{
            Name_Email.style.borderColor = 'red';
            User_Name_Email = false;
            Name_Email.setCustomValidity("enter a valid name");
        }

    } 

    else if (Data_type == 'button'){
        if (User_Name_Email && Password_valid) {
            form.submit()
        }
        else{
            Name_Email.style.borderColor = 'red';
            Password.style.borderColor = 'red';

            alert("Enter valid data before enter !")
        }

        if(Password.value.length < 7){
            alert("Password is too short. password must be greater than 6 characters")
        }
    }
    
    else {

        if (Password.value.length > 6 ){
            Password.style.borderColor = "gray";
            Password.setCustomValidity("");
            Password_valid = true;
        }

        else{
            Password.style.borderColor = "red";
            Password.setCustomValidity("Password is too short");
            Password_valid = false;
        
        }
    }
}



Name_Email.addEventListener("input",function(){
    Process("Name")
});
Password.addEventListener("input",function(){
    Process("Password")
});

Button.addEventListener("click",function(){
    Process("button")
});

form.addEventListener("submit",function(event){
        event.preventDefault()
    });
