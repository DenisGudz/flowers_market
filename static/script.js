
function onAdd() {

    const xhr = new XMLHttpRequest()
    xhr.open('POST', '/signup')
    xhr.setRequestHeader('Content-type', 'application/json');


    const username = document.querySelector('.username').value
    const password = document.querySelector('.password').value
    const passwordCheck = document.querySelector('.passwordCheck').value
    xhr.onreadystatechange = function () {
        if (this.readyState === 4) {


            if (this.status === 200) {
                const data = JSON.parse(this.responseText)
                console.log('data:', data)
                window.location.href = "http://127.0.0.1:5000/loginpage";

               
                



            } else {
                console.log("error: " + this.status)
            }
            // console.log(JSON.parse(this.responseText))
        }
    }
    if (password===passwordCheck) {
        xhr.send(JSON.stringify({ "to_add": [username, password]}))
     } else {
        alert('the password')
     }
}



function onLogin() {

    const xhr = new XMLHttpRequest()
    xhr.open('POST', '/login')
    xhr.setRequestHeader('Content-type', 'application/json');


    const username = document.querySelector('.usernameLogin').value
    const password = document.querySelector('.passwordLogin').value

    xhr.onreadystatechange = function () {
        if (this.readyState === 4) {


            if (this.status === 200) {
                const data = JSON.parse(this.responseText)
                console.log('data:', data)


                    if(data==="successfuly"){
                        window.location.href = "http://127.0.0.1:5000/home"
                    } else{
                        alert('there is no such account')
                    }
            

               
            
            } else {
                console.log("error: " + this.status)
            }
            // console.log(JSON.parse(this.responseText))
        }
    }
    
        xhr.send(JSON.stringify({ "to_add": [username, password]}))
}





function onLogout() {
    const xhr = new XMLHttpRequest()
    xhr.open('POST', '/logout')
    xhr.setRequestHeader('Content-type', 'application/json');

    xhr.onreadystatechange = function () {
        if (this.readyState === 4) {

            if (this.status === 200) {
                window.location.href = "http://127.0.0.1:5000/login"
                

            } else {
                console.log("error: " + this.status)
            }
            // console.log(JSON.parse(this.responseText))
        }
    }
    
        xhr.send(JSON.stringify("asdf"))
}
