
let Edit_Button = document.getElementById("Edit-Button"),
Import_Button = document.getElementById("Button"),
Dialog = document.getElementById("Dialog"),
Dialog_cancel = document.getElementById("Button-Dialog-cancel"),
Dialog_OK = document.getElementById("Button-Dialog-ok"),
Dialog_form= document.getElementById("Dialog-Form"),
Csv_Parent = document.getElementById("User-imforamtion-csv-parent");



function Create_Div(Name ,Last,Email,Lang,Type,Topic){

    let Parent = document.getElementById('User-imforamtion-Parent');
    let div = document.createElement('div');
    div.className = 'User-imformation';
    div.id = 'User-imformation';

    let Subdiv= document.createElement("div");
    Subdiv.className = "user-imf-div";

    Parent.appendChild(div);
    div.appendChild(Subdiv);
    
    let h1 = document.createElement('h4');
    h1.textContent = Name + Last;
    h1.className = 'user-imformation-h4';
    Subdiv.appendChild(h1);

    let EmailDiv = document.createElement("div");
    EmailDiv.className = "user-imf-div";
    div.appendChild(EmailDiv);
    let h2 = document.createElement('h4');
    h2.textContent = Email;
    h2.className = 'user-imformation-h4';
    h2.style.paddingLeft = "10px";
    h2.style.paddingRight = "10px";
    EmailDiv.appendChild(h2);

    let LangDiv = document.createElement("div");
    LangDiv.className = "user-imf-div";
    div.appendChild(LangDiv);
    let h3 = document.createElement('h4');
    h3.textContent = Lang;
    h3.className = 'user-imformation-h4';
    LangDiv.appendChild(h3);

    let TypeDiv = document.createElement("div");
    TypeDiv.className = "user-imf-div";
    div.appendChild(TypeDiv);
    let h4 = document.createElement('h4');
    h4.textContent = Type;
    h4.className = 'user-imformation-h4';
    TypeDiv.appendChild(h4);

    let TopicDiv = document.createElement("div");
    TopicDiv.className = "user-imf-div";
    div.appendChild(TopicDiv);
    let h5 = document.createElement('h4');
    h5.textContent = Topic;
    h5.className = 'user-imformation-h4';
    TopicDiv.appendChild(h5);

    let EditDiv = document.createElement("div");
    EditDiv.className = "user-imf-div";
    EditDiv.style.border = "0";
    div.appendChild(EditDiv);
    let h6 = document.createElement('button');
    h6.id = 'Edit-Button';
    h6.innerText = "Edit";
    EditDiv.appendChild(h6);
}

function Create_Csv_Div(Name,Last,Email,Lang,Status,Topic) {

    let div = document.createElement('div');
    div.className = 'User-imformation-csv';
    div.id = 'User-imformation-csv';

    let Subdiv= document.createElement("div");
    Subdiv.className = "user-imf-div";

    Csv_Parent.appendChild(div);
    div.appendChild(Subdiv);
    
    let h1 = document.createElement('h4');
    h1.textContent = Name + Last;
    h1.className = 'user-imformation-h4';
    Subdiv.appendChild(h1);

    let EmailDiv = document.createElement("div");
    EmailDiv.className = "user-imf-div";
    div.appendChild(EmailDiv);
    let h2 = document.createElement('h4');
    h2.textContent = Email;
    h2.className = 'user-imformation-h4';
    h2.style.paddingLeft = "10px";
    h2.style.paddingRight = "10px";
    EmailDiv.appendChild(h2);

    let LangDiv = document.createElement("div");
    LangDiv.className = "user-imf-div";
    div.appendChild(LangDiv);
    let h3 = document.createElement('h4');
    h3.textContent = Lang;
    h3.className = 'user-imformation-h4';
    LangDiv.appendChild(h3);

    let TypeDiv = document.createElement("div");
    TypeDiv.className = "user-imf-div";
    div.appendChild(TypeDiv);
    let h4 = document.createElement('h4');
    h4.textContent = Status;
    h4.className = 'user-imformation-h4';
    TypeDiv.appendChild(h4);

    let TopicDiv = document.createElement("div");
    TopicDiv.className = "user-imf-div";
    TopicDiv.style.border = "0"
    div.appendChild(TopicDiv);
    let h5 = document.createElement('h4');
    h5.textContent = Topic;
    h5.className = 'user-imformation-h4';
    TopicDiv.appendChild(h5);

}


for(let i = 1; i <= Total ; i++){

    fetch('/return-data', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({"return" : i})
    })
    .then(response => response.json())
    .then(data => {
    Name = data['Name'];
    Last = data['Last'];
    Email = data['Email'];
    Lang = data['Lang'];
    Topic = data['Topic'];
    Type = data['Type'];

    Create_Div(Name,Last,Email,Lang,Type,Topic);
})

}

Import_Button.addEventListener("click",function(){
    Dialog.showModal();
    Dialog_cancel.addEventListener("click",function(){
        Dialog.close();
    });

    Dialog_OK.addEventListener('click',function(){
        Dialog_form.submit();
    });
});


for(let i = 1; i <= Total_Csv ; i++){

    fetch('/return-csv-data', {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify({"return" : i})
    })
    .then(response => response.json())
    .then(data => {

        if(data['exist']){
            Name = data['Name'];
            Last = data['Last'];
            Email = data['Email'];
            Lang = data['Lang'];
            Topic = data['Topic'];
            Status = data["Status"]

            Create_Csv_Div(Name,Last,Email,Lang,Status,Topic);
        }


})

}
