let Imformation_Div = document.getElementById("User-imformation"),
Edit_Button = document.getElementById("Edit-Button"),
Parent = document.getElementById('User-imforamtion-Parent');


Edit_Button.addEventListener('click',function(){
    Parent.append(Imformation_Div);
});
