function singin() {

    const xhr = new XMLHttpRequest()
    xhr.open('POST', './singinFunction')
    xhr.setRequestHeader('Content-type', 'application/json');
    
        // Get the drop area element
    const username  = document.querySelector('.name').value
    const password  = document.querySelector('.password').value
    const passwordReCheck  = document.querySelector('.passRecheck').value
    // console.log(username)
    xhr.onreadystatechange = function () {
        if (this.readyState === 4) {
            
            if (this.status === 200) {
                console.log('hello wotld')
                const data = this.responseText 
                console.log("data:",data)       

                if (data === "success"){
                    window.location.href = "/login"
                }
            } else {
                +-                console.log("error: " + this.status)
            }
            // console.log(JSON.parse(this.responseText))
        }
    }
        if (password === passwordReCheck){
        xhr.send(JSON.stringify({"name":username, "password":password}))
        } else{
            alert('the passwords are no identical')
            console.log('the passwords arent identical')
        }
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
