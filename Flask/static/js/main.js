// let Account = '{{Account}}';
let Content = document.getElementById("content");
let Profile = document.getElementById("Profile");
let Update_Button = document.getElementById("Sign-Div");
let Sign_Button = document.getElementById("Sign");
let Log_Button = document.getElementById("Log");
let Log_out_Button = document.getElementById("Log-out");
let Name_P = document.getElementById('SSS');
let update_form =document.getElementById('update_form'), Up_Button = document.getElementById("up_but"),
Dialog = document.getElementById("Dialog") , Dialog_Button = document.getElementById("Dialog-Button"),
Dialog_cancel_Button = document.getElementById('Dialog-Cancel-Button');

let User_Input = document.getElementById('username') , last_Input = document.getElementById('lastname'),
Email_Input = document.getElementById('email'),Lang_Input = document.getElementById('lang') 
,Topic_Input = document.getElementById('topic'),Dialog_Form = document.getElementById("Dialog-Form"),
Delete_Button = document.getElementById("Delete-Button"),Delete_Dialog = document.getElementById("Delete-Dialog");

User_Input.value = Name ;
last_Input.value = Last;
Email_Input.value = Email;
Lang_Input.value = Lang;
Topic_Input.value = Topic;


if (Account) {
    Name_P.innerText = Name[0]
    Sign_Button.remove();
    Log_Button.remove()

} else {
    Content.remove();
    Profile.remove();
    Update_Button.remove();
    Log_out_Button.remove();
}

function update() {
    Dialog.showModal()
    Dialog_cancel_Button.addEventListener('click',function(){
            Dialog.close();
    })
    
}

update_form.addEventListener('submit',function(event){
    event.preventDefault();
});

Up_Button.addEventListener('click',update);

var n = true,l = true, e = true;

function User_Input_Name(){
    if (isNaN(User_Input.value)) {
        User_Input.style.borderColor ="black";
        n = true;
    } else {
        User_Input.style.borderColor ="red";
        User_Input.style.borderStyle = 'solid'
        n = false;
    }
}

function User_Input_Last() {
    if (isNaN(last_Input.value)) {
        last_Input.style.borderColor ="black";
        l = true;
    } else {
        last_Input.style.borderColor ="red";
        last_Input.style.borderStyle = 'solid';
        l = false;
    }
}

function User_Input_Email (){
    if (isNaN(Email_Input.value)) {
        Email_Input.style.borderColor ="black";

        if (Email_Input.value.includes('@') && Email_Input.value.includes('.com') ) {
            Email_Input.style.borderColor ="black";
            e = true;
        } else {
            Email_Input.style.borderColor ="red";
            Email_Input.style.borderStyle = 'solid';
            e = false;
        }
    } else {
        Email_Input.style.borderColor ="red";
        Email_Input.style.borderStyle = 'solid';
        e = false;
    }
}


User_Input.addEventListener('input',User_Input_Name);
last_Input.addEventListener('input',User_Input_Last);
Email_Input.addEventListener('input',User_Input_Email);
Dialog_Form.addEventListener('submit',function(event){
    event.preventDefault()
});

Dialog_Button.addEventListener('click',function(){
    if (n && l && e ){
        Dialog_Form.submit()
    } else {
        User_Input.style.borderColor ="red";
        User_Input.style.borderStyle = 'solid';
        last_Input.style.borderColor ="red";
        last_Input.style.borderStyle = 'solid';
        Email_Input.style.borderColor ="red";
        Email_Input.style.borderStyle = 'solid';
    }
});

Delete_Button.addEventListener("click",function(event){
    event.preventDefault();
    Delete_Dialog.showModal()

    let CAncel_Buttton = document.getElementById('d-cancel');

    CAncel_Buttton.addEventListener("click",function(){
        Delete_Dialog.close()

    });

});