const postObject = document.querySelector(".button-upload");
const formObject = document.querySelector(".frame-form");
const crossObject = document.querySelector(".cross");
const dotsList = document.querySelectorAll(".dots-post");
const dotsFormList = document.querySelectorAll(".dot-form");
const wrapperList = document.querySelectorAll(".redact-wrapper");
const bodyObject = document.querySelector(".full-screen");

postObject.addEventListener("click", function(event){
    event.preventDefault();
    formObject.classList.toggle("hidden");
    bodyObject.classList.toggle("blur");
})

crossObject.addEventListener("click", function(event){
    formObject.classList.toggle("hidden");
    bodyObject.classList.toggle("blur");
})

for (let count = 0; count < dotsList.length; count ++){
    let dotsObject = dotsList[count];
    let wrapperObject = wrapperList[count]
    dotsObject.addEventListener("click", function(event){
        event.preventDefault();
        wrapperObject.classList.toggle("hidden")
    })
}
for (let count = 0; count < dotsFormList.length; count ++){
    let dotsObject = dotsFormList[count];
    let wrapperObject = wrapperList[count]
    dotsObject.addEventListener("click", function(event){
        event.preventDefault();
        wrapperObject.classList.toggle("hidden")
    })
}

