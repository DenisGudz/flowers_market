
function isLoged() {
    
    let banner = 'static/banner.png'
    let slogan = 'Blooming Beauty Delivered to Your Doorstep!'
    const sloganElement = document.querySelector(".slogan")
    const sloganElsafdement = document.querySelector(".slogan")
      
    let urlParams = new URLSearchParams(window.location.search);
    let arg1 = urlParams.get('arg1');
    console.log(arg1)
    
}




isLoged()






function onLogout() {
  const xhr = new XMLHttpRequest()
  xhr.open('POST', '/logout')
  xhr.setRequestHeader('Content-type', 'application/json');
  console.log('hello world')
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




// function homeProducts() {
//   const xhr = new XMLHttpRequest()
//   xhr.open('POST', '/homeProducts')
//   xhr.setRequestHeader('Content-type', 'application/json');
//   xhr.onreadystatechange = function () {
//     if (this.readyState === 4) {
      
//       if (this.status === 200) {  
//         console.log(JSON.parse(this.responseText))
//       }
//     }
    
//   }
//   console.log("hello mir")
//   xhr.send(JSON.stringify("asdf"))
// }

// homeProducts()