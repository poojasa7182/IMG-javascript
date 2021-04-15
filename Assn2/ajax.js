function load(id , url){
    var ajaxObject = null;

    if(window.XMLHttpRequest){
        ajaxObject = new XMLHttpRequest();
    }
    else{
        if(window.ActiveXObject){
            ajaxObject = new ActiveXObject("Microsoft.XMLHTTP")
        }
    }

    if(ajaxObject != null){
        ajaxObject.open("GET" , url , true );
        ajaxObject.send();
    }
    else{
        alert("You donot have a compatible browser.")
    }
    ajaxObject.onreadystatechange = function(){
        if(ajaxObject.readyState==4 && ajaxObject.status==200){
            var siteData = JSON.parse(ajaxObject.responseText);
            console.log(siteData);
            
            var siteData_data = siteData.data;
            //console.log(siteData_data);

            for(let i =  0 ; i < (siteData_data).length ; i++){
                let mainDiv = document.createElement("div");
                
                let childDiv1 = document.createElement("div");
                childDiv1.innerHTML=siteData_data[i].first_name;
                mainDiv.appendChild(childDiv1);
                
                let childDiv2 = document.createElement("div");
                childDiv2.innerHTML=siteData_data[i].last_name;
                mainDiv.appendChild(childDiv2);

                let childDiv3 = document.createElement("div");
                childDiv3.innerHTML=siteData_data[i].email;
                mainDiv.appendChild(childDiv3);

                let childDiv4 = document.createElement("div");
                let photo = document.createElement("img");
                photo.src = siteData_data[i].avatar;
                childDiv4.appendChild(photo);
                mainDiv.appendChild(childDiv4);

                let childDiv5 = document.createElement("div");
                childDiv5.innerHTML=siteData_data[i].id;
                mainDiv.appendChild(childDiv5);

                document.getElementById(id).appendChild(mainDiv);
            }
        }
        
    };
    
}