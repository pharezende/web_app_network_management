async function getRouter(value) {
    const response = await fetch('http://127.0.0.1:5000/routers/single/'+value);
    const myJson = await response.json(); //extract JSON from the http response
    return myJson;
}


async function getRouters() {
    var params = {
        method: 'GET'
        };

    const response = await fetch('http://127.0.0.1:5000/routers/all/', params);
    const myJson = await response.json(); //extract JSON from the http response
    return myJson;
}

 function processFunctionality(funcionality) {
    //Single
    if (funcionality == "get_router") {
        //Method GET
        return getRouters()
    }
    if (funcionality == "get_routers") {
        //Method GET
        return getRouters()
    }
}

function isSingle(url){
    if (url == "get_router" || url == "get_switch" || url == "get_host" || url == "get_link"){
        return true;
    }
    return false;
}

function callForm(url){
    switch (url){
        case 'get_router':
            var element = document.querySelector('.content');
            element.innerHTML = "<form id='form_get_router' action='javascript:getRouter(rname.value)'> " +
                "<label for='router_name'>Router:</label><br>" +
                "<input type='text' id='rname' name='rname'/><br /> " +
                "<input type='submit' value='submit'>";
    }
}


function getMethod(url){
    var params = {
        method: 'GET'
        };

}

function postMethod(url){
    var params = {
        method: 'POST'
        };

}

function deleteMethod(url){
    var params = {
        method: 'DELETE'
        };

}
