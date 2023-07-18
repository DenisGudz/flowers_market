




function add() {
  const cookie = document.cookie
  if (!cookie){
      window.location.href = "/login"
  }
}

add()


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

function onImageSelected(event) {
  const fileReader = new FileReader()
   const file = event.target.files[0]
   const id = event.target.parentElement.id
   console.log(id)
   console.log(file)
  fileReader.onload = (e)=>{
    const imageUrl = e.target.result
    const imgContainer = document.querySelector(`#${id}`);
    imgContainer.style.backgroundImage = "url('" + imageUrl + "')";
    
  }
  fileReader.readAsDataURL(file);
}

// Get the drop zone element
function upload() {
  const xhr = new XMLHttpRequest();
  xhr.open('POST', '/upload', true);
    
    const fileInput1 = document.getElementById('fileToUpload1');
    const fileInput2 = document.getElementById('fileToUpload2');
    const fileInput3 = document.getElementById('fileToUpload3');
    const file1 = fileInput1.files[0];
    const file2 = fileInput2.files[0];
    const file3 = fileInput3.files[0];


    const formData = new FormData();
    const price = document.querySelector('.productPrice').value
    const name = document.querySelector('.productName').value
    formData.append('files[]', file1);
    formData.append('files[]', file2);
    formData.append('files[]', file3);
    formData.append('data', JSON.stringify({'name': name,'price': price}))
    
    console.log(price)
    console.log(name)
    
    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4 && xhr.status === 200) {
        // File upload completed successfully
        const data = this.responseText
        console.log(data)
        alert(data)
        inputs = document.querySelectorAll("input")
        inputs.forEach(element => {
          element.value = ""
        });
        window.location.reload()

      }
    };

    
    xhr.onerror = function() {
      // Error occurred during file upload
      console.error('An error occurred during file upload.');
    };
    
    xhr.send(formData);
  }
