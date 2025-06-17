const buttonCreateGroup = document.querySelector('.button-title');
const formObject = document.querySelector(".modal-create-group");
const frameCross = document.querySelector(".frame-cross");
const fullscreen = document.querySelector(".fullscreen");


buttonCreateGroup.addEventListener("click", ()=>{
    formObject.classList.toggle("hidden");
    fullscreen.classList.toggle("hidden");
})
frameCross.addEventListener("click", ()=>{
    formObject.classList.toggle("hidden");
    fullscreen.classList.toggle("hidden");
})