function isLoged() {
    const cookie = document.cookie
    if (!cookie){
        window.location.href = "/login"
    }
}

isLoged()




function upload() {
    console.log('asdf')
    const xhr = new XMLHttpRequest()
    xhr.open('POST', '/update')
    //xhr.setRequestHeader("Content-Type", "multipart/form-data");
    const formData = new FormData();

    const slogan = document.querySelector('.slogan').value || ''
    const banner = document.querySelector(".banner")
    const bannerFile = banner.files[0];

    console.log(banner)
    console.log(bannerFile)
    console.log(slogan, 'slogan')

    formData.append('file', bannerFile);
    formData.append('data', JSON.stringify({'slogan': slogan}))

    xhr.onreadystatechange = function () {
        if (this.readyState === 4) {


            if (this.status === 200) {
                const data = this.responseText
                // console.log('data:', data)
                alert(data)

                    // if(data==="successfuly"){
                    //     window.location.href = "http://127.0.0.1:5000/home"
                    // } else{
                    //     alert('there is no such account')
                    // }
            

            
            
            } else {
                console.log("error: " + this.status)
            }
            // console.log(JSON.parse(this.responseText))
        }
    }
        // 
        console.log(formData)
        xhr.send(formData)
}



// function upload() {
//     console.log('asdf')
//     const xhr = new XMLHttpRequest()
//     xhr.open('POST', '/update')
//     //xhr.setRequestHeader("Content-Type", "multipart/form-data");


//     xhr.onreadystatechange = function () {
//         if (this.readyState === 4) {


//             if (this.status === 200) {
//                 const data = this.responseText
//                 // console.log('data:', data)
//                 alert(data)

            
//             } else {
//                 console.log("error: " + this.status)
//             }
//             // console.log(JSON.parse(this.responseText))
//         }
//     }
//         // 
//         console.log(formData)
// }



function onRemove(event) {
    const xhr = new XMLHttpRequest()
    xhr.open('POST', '/remove')
    xhr.setRequestHeader('Content-type', 'application/json');
    productElement = event.target.parentElement.className
    console.log(productElement)
    productId = productElement.substring("productElement prodcut".length)
    console.log(productId)
    


    xhr.onreadystatechange = function () {
        if (this.readyState === 4) {


            if (this.status === 200) {
                const data = this.responseText
                alert(data)
                location.reload()


            

            
            
            } else {
                console.log("error: " + this.status)
            }
            // console.log(JSON.parse(this.responseText))
        }
    }
        // 
        
        xhr.send(JSON.stringify({ "id" :  productId}))
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
