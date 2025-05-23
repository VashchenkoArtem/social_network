document.addEventListener("DOMContentLoaded", function () {
    const postObject = document.querySelector(".button-upload");
    const formObject = document.querySelector(".frame-form");
    const crossObject = document.querySelector(".cross");
    const dotsList = document.querySelectorAll(".dots-post");
    const dotsFormList = document.querySelectorAll(".dot-form");
    const wrapperList = document.querySelectorAll(".redact-wrapper");
    const bodyObject = document.querySelector(".full-screen");
    const crossesRedact = document.querySelectorAll(".cross-redact");
    const formsRedact = document.querySelectorAll(".redact-post-function");
    const redactButtons = document.querySelectorAll(".redacting-title-redact");

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

    for (let count = 0; count < redactButtons.length; count++) {
        let buttonRedact = redactButtons[count];
        let formRedact = formsRedact[count];
        buttonRedact.addEventListener("click", () => {
            formRedact.classList.toggle("hidden");
            bodyObject.classList.toggle("blur");
        });
    }

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
                    const bin = document.createElement("img");
                    bin.src = "/../images/"
                    img.src = event.target.result;
                    img.classList.add("post-images-form")
                    previewDiv.appendChild(img);
                };
                reader.readAsDataURL(file);
            });
        });
    }
});