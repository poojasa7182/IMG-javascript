function producePrompt(message ,promptLocation,color){
    document.getElementById(promptLocation).innerHTML = message;
    document.getElementById(promptLocation).style.color = color;
}
function nowOk(promptLocation){
    document.getElementById(promptLocation).innerHTML = "";
}

function load(){
    let email = document.getElementById("Email");
    let pass = document.getElementById("password");
    var emailE = email.value;
    if(!emailE.match(/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+.([a-zA-Z0-9-]+)$/)){
        producePrompt("Invalid Email!!" , "emailPrompt" , "red");
        return false;
    }
    else{
        nowOk("emailPrompt");
        if(emailE=="eve.holt@reqres.in"&&pass.value=="cityslicka"){
            let xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function(){
            if(xhttp.readyState==4 && xhttp.status==200){
                let response = JSON.parse(this.response);
                alert("The tokken is:"+response["token"])
            }
            else{
                alert("error");
            }
        }
        xhttp.open("POST"," https://reqres.in/api/login",true);
        xhttp.setRequestHeader('Content-type','application/x-www-form-urlencoded')
        xhttp.send(`email=${emailE}&password=${pass.value}`)
        return true;
        }
        else{
            alert("invalid credentials");
        }
        
    }  
}