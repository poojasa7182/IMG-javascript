//common functions
function producePrompt(message ,promptLocation,color){
    document.getElementById(promptLocation).innerHTML = message;
    document.getElementById(promptLocation).style.color = color;
}
function nowOk(promptLocation){
    document.getElementById(promptLocation).innerHTML = "";
}



//name
function validateName(){
    var nameE = document.getElementById("name").value;
    var name = nameE.trim();
    if(name.length==0){
        producePrompt("Name is required!!" , "namePrompt" , "red");
        return false;
    }
    if(!name.match(/^[a-zA-Z\s']+$/)){
        producePrompt("Invalid Name!!" , "namePrompt" , "red");
        return false;
    }
    else{
        nowOk("namePrompt");
        return true;
    }   
}
//E-mail
function validateEmail(){
    var emailE = document.getElementById("Email").value;
    var email = emailE.trim();
    if(email.length==0){
        producePrompt("Email is required!!" , "emailPrompt" , "red");
        return false;
    }
    if(!email.match(/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+\.([a-zA-Z0-9-.]+)[a-zA-Z]$/)){
        producePrompt("Invalid Email!!" , "emailPrompt" , "red");
        return false;
    }
    else{
        nowOk("emailPrompt");
        return true;
    }   

}
//Password
function validatePass(){
    var passE = document.getElementById("Password").value;
    var pass = passE.trim();
    if(pass.match(/^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})/)){
        producePrompt("Strong Password" , "passPrompt" , "green");
        return true;
    }
    if(pass.length<=5){
        producePrompt("Password must contain atleast 6 characters" , "passPrompt" , "red");
        return false;
    }
    // if(!pass.match(/^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[!@#\$%\^&\*]))|((?=.*[a-z])(?=.*[!@#\$%\^&\*]))|((?=.*[a-z])(?=.*[A-Z])(?=.*[!@#\$%\^&\*]))|((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])))(?=.{,5})/)){
    //     producePrompt("Password must contain atleast 6 characters" , "passPrompt" , "red");
    //     return false;
    // }
    // if(!pass.match(/^(((?=.*[!@#\$%\^&\*])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[!@#\$%\^&\*])(?=.*[0-9]))|((?=.*[a-z])(?=.*[!@#\$%\^&\*])(?=.*[0-9])))(?=.{,5})/)){
    //     producePrompt("Password must contain atleast 6 characters" , "passPrompt" , "red");
    //     return false;
    // }
    if(pass.match(/^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[!@#\$%\^&\*]))|((?=.*[a-z])(?=.*[!@#\$%\^&\*]))|((?=.*[a-z])(?=.*[A-Z])(?=.*[!@#\$%\^&\*]))|((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])))(?=.{6,})/)){
        producePrompt("Weak Password" , "passPrompt" , "red");
        return true;
    }
    if(pass.match(/^((?=.*[a-z])|(?=.*[A-Z])|(?=.*[0-9])|(?=.*[!@#\$%\^&\*])|((?=.*[!@#\$%\^&\*])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[!@#\$%\^&\*])(?=.*[0-9]))|((?=.*[a-z])(?=.*[!@#\$%\^&\*])(?=.*[0-9])))(?=.{6,})/)){
        producePrompt("Weak Password" , "passPrompt" , "red");
        return true;
    }
}
//ConfirmPassword
function validateCoPass(){
    var copass = document.getElementById("Confirm-password").value;
    var pass = document.getElementById("Password").value;
    if(copass!=pass){
        producePrompt("Password doesnt match" , "coPassPrompt" , "red");
        return false;
    }
    else{
        nowOk("coPassPrompt");
        return true; 
    }
}
//Age
function validateAge(){
    var ageE = document.getElementById("Age").value;
    var age = ageE.trim();
    if(age.length==0){
        producePrompt("Age is required!!" , "agePrompt" , "red");
        return false;
    }
    if(!age.match(/^[0-9]+$/)){
        producePrompt("Invalid format" , "agePrompt" , "red");
        return false;
    }
    else{
        if(age<18){
            producePrompt("Minimum age required is 18" , "agePrompt" , "red");
            return false;
        }
        else{
            nowOk("agePrompt");
            return true;  
    
        }
    }
}
//PhoneNo.
function validatePhnNo(){
    var phnE = document.getElementById("phnNo").value;
    var phn = phnE.trim();
    if(phn.length==0){
        producePrompt("Phone number is required!!" , "phnNoPrompt" , "red");
        return false;
    }
    if(phn.length>10){
        producePrompt("Invalid Phone Number!!" , "phnNoPrompt" , "red");
        return false;
    }
    if(!phn.match(/^[0-9]+$/)){
        producePrompt("Invalid format" , "phnNoPrompt" , "red");
        return false;
    }
    else{
        nowOk("phnNoPrompt");
        return true;      
    }
}
//City
function validateCity(){
    var cityE = document.getElementById("City").value;
    var city = cityE.trim();
    if(city.length==0){
        producePrompt("City is required!!" , "cityPrompt" , "red");
        return false;
    }
    if(!city.match(/^[a-zA-Z\s]+$/)){
        producePrompt("Invalid format" , "cityPrompt" , "red");
        return false;
    }
    else{
        nowOk("cityPrompt");
        return true;      
    }
}
//Edu
function validateEdu(){
    var edu = document.getElementById("edu").value;
    if(edu.length==0){
        producePrompt("Educational Qualification is required!!" , "eduPrompt" , "red");
        return false;
    }
    else{
        nowOk("eduPrompt");
        return true;      
    }
}
//gender
function validateGen(){
    var gen = document.forms["forms"]["gender"];
    if(gen[0].checked==false&&gen[1].checked==false&&gen[2].checked==false){
        producePrompt("Gender is required!!" , "genPrompt" , "red");
        return false;
    }
    else{
        nowOk("genPrompt");
        return true;      
    }
}
//validate all
function validate(){
    if(validateGen()&&validateEdu()&&validateCity()&&validatePhnNo()&&validateAge()&&validateCoPass()&&validatePass()&&validateEmail()&&validateName()){

    }
    else{
        alert("All fields not filled")
    }
}