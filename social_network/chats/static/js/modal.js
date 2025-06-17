const buttonCreateGroup = document.querySelector('.button-title');
const formObject = document.querySelector(".modal-create-group");
const frameCross = document.querySelector(".frame-cross");
const fullscreen = document.querySelector(".fullscreen");
const groupModal = document.querySelector(".modal-set-name");
const buttonCreate = document.querySelector(".confirm-create-group")


buttonCreateGroup.addEventListener("click", ()=>{
    formObject.classList.toggle("hidden");
    fullscreen.classList.toggle("hidden");
})
frameCross.addEventListener("click", ()=>{
    formObject.classList.toggle("hidden");
    fullscreen.classList.toggle("hidden");
})
const cookies = document.cookie.split(';')
for (let cookieField of cookies){
    if (cookieField.includes("group_members")){
        groupModal.classList.toggle("hidden")
    }
}
console.log(cookies)