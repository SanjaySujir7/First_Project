let Account = true;
let Content = document.getElementById("content");
let Profile = document.getElementById("Profile");
let Update_Button = document.getElementById("Sign-Div");
let Sign_Button = document.getElementById("Sign");
let Log_Button = document.getElementById("Log");
let Log_out_Button = document.getElementById("Log-out");


if (Account) {
    Sign_Button.remove();
    Log_Button.remove()

} else {
    Content.remove();
    Profile.remove();
    Update_Button.remove();
    Log_out_Button.remove();
}