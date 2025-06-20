const buttonRedact = document.querySelector(".edit-2");
const screenDiv = document.querySelector(".screen")
const buttonSave = document.querySelector(".save-info-button")
const eyeImages = document.querySelectorAll(".eye-img");
const editButton = document.querySelector('.edit-info-button');
const editProfileCard = document.querySelector(".edit-profile-card");
const defaultCard = document.querySelector(".default-profile-card");
const inputImage = document.querySelector(".change-avatar")
const imageAvatar = document.getElementById('user-img');


for (let count = 0; count < eyeImages.length; count++){
    let eyeImage = eyeImages[count];
    let input = document.getElementById(eyeImage.id)
    eyeImage.addEventListener("click", (event)=>{
        if (eyeImage.src.includes("eye.png")){
            eyeImage.src += "/../eye_close.png"
            
            input.type = "password"
        }
        else if (eyeImage.src.includes("eye_close.png")){
            eyeImage.src += "/../eye.png"
            input.type = "text"
        }
    })
    if (input.name.includes("password1") || input.name.includes("password2") || input.name.includes("password")){
        eyeImage.src += "/../eye_close.png"
    }
}

buttonRedact.addEventListener("click", ()=>{
    screenDiv.classList.toggle("hidden")
    buttonRedact.classList.toggle("hidden")
    buttonSave.classList.toggle("hidden")
})

editButton.addEventListener('click', function(){
    defaultCard.classList.toggle("hidden")
    editProfileCard.classList.toggle('hidden');
})
inputImage.addEventListener('change', function() {
    const image = inputImage.files[0];
    const reader = new FileReader();
    
    reader.addEventListener('load', function() {
        imageAvatar.src = reader.result;
    });
    reader.readAsDataURL(image);
});