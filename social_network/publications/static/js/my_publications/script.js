const postObject = document.querySelector(".button-upload");
const formObject = document.querySelector(".frame-form");
const crossObject = document.querySelector(".cross");
const dotsList = document.querySelectorAll(".dots-post");
const dotsFormList = document.querySelectorAll(".dot-form");
const wrapperList = document.querySelectorAll(".redact-wrapper");
const bodyObject = document.querySelector(".full-screen");
const crossesRedact = document.querySelectorAll(".cross-redact");
const formsRedact = document.querySelectorAll(".redact-post-function");
const redactButtons = document.querySelectorAll(".redacting-title");
const wrapperRedact = document.querySelectorAll(".redact-post")


postObject.addEventListener("click", function (event) {
    event.preventDefault();
    formObject.classList.toggle("hidden");
    bodyObject.classList.toggle("blur");
});
crossObject.addEventListener("click", function (event) {
    formObject.classList.toggle("hidden");
    bodyObject.classList.toggle("blur");
});
for (let count = 0; count < dotsList.length; count++) {
    let dotsObject = dotsList[count];
    let wrapperObject = wrapperList[count];
    dotsObject.addEventListener("click", function (event) {
        event.preventDefault();
        wrapperObject.classList.toggle("hidden");
    });
}
for (let count = 0; count < dotsFormList.length; count++) {
    let dotsObject = dotsFormList[count];
    let wrapperObject = wrapperList[count];
    dotsObject.addEventListener("click", function (event) {
        event.preventDefault();
        wrapperObject.classList.toggle("hidden");
    });
}
redactButtons.forEach(element => {
    let formRedact = formsRedact[element.id ];
    let wrapperObject = wrapperRedact[element.id];

    element.addEventListener("click", () => {
        formRedact.classList.toggle("hidden");
        bodyObject.classList.toggle("blur");
        wrapperObject.classList.toggle("hidden");
        $.ajax({
            url: `/check_info_post/${element.id}`,
            type: 'POST',
            data: {
                'pk': element.id,
                'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            success: function(response){
                let post = JSON.parse(response)[0]["fields"]
                document.querySelectorAll("#field-title")[element.id].value = post['title']
                document.querySelectorAll("#field-topic")[element.id].value = post['topic']
                document.querySelectorAll("#field-text")[element.id].value = post['text']
                document.querySelectorAll("#field-url")[element.id].value = post['url']
            }
        })
        
    });
})



for (let count = 0; count < crossesRedact.length; count++) {
    let crossRedact = crossesRedact[count];
    let formRedact = formsRedact[count];
    crossRedact.addEventListener("click", () => {
        formRedact.classList.toggle("hidden");
        bodyObject.classList.toggle("blur");
    });
}
const input = document.querySelector("#image-to-post-form");
const previewDiv = document.querySelector("#image-preview-container");
if (input && previewDiv) {
    input.addEventListener("change", function () {
        previewDiv.innerHTML = "";
        const files = Array.from(input.files);
        files.forEach(file => {
            if (!file.type.startsWith("image/")) return;
            const reader = new FileReader();
            reader.onload = function (event) {
                const img = document.createElement("img");
                img.src = event.target.result;
                img.classList.add("post-images-form")
                previewDiv.appendChild(img);
            };
            reader.readAsDataURL(file);
        });
    });
};
