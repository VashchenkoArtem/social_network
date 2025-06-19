const buttonCreateGroup = document.querySelector('.button-title');
const formObject = document.querySelector(".modal-create-group");
const frameCross = document.querySelector(".frame-cross");
const fullscreen = document.querySelector(".fullscreen");
const groupModal = document.querySelector(".modal-set-name");
const buttonCreate = document.querySelector(".confirm-create-group");
const inputImage = document.getElementById("add-image-avatar");
const imageAvatar = document.querySelector(".group-image");
const editFormName = document.querySelector(".edit-form-name");
const dots = document.querySelector(".dots");
const addMemberButton = document.querySelector(".add-member-button");
const editFormMembers = document.querySelector(".modal-edit-group");
const editGroup = document.querySelector(".confirm-create-group");
const crossImage = document.querySelector(".close-second-modal");

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
        fullscreen.classList.toggle("hidden");
        groupModal.classList.toggle("hidden");
    }
}
inputImage.addEventListener('change', function(){
    let image = inputImage.files[0];
    let reader = new FileReader();
    reader.addEventListener('load', function(){
        imageAvatar.src = reader.result;
    })
    reader.readAsDataURL(image);
})
if (dots){
    dots.addEventListener('click', function(){
        editFormName.classList.toggle("hidden");
        fullscreen.classList.toggle("hidden");
    })

}
if (addMemberButton){
    addMemberButton.addEventListener('click', function(){
        editFormName.classList.toggle("hidden");
        editFormMembers.classList.toggle("hidden");
        fullscreen.classList.toggle("hidden");
})
}

for (let field of cookies){
    if (field.includes("get_friends")){
        editFormName.classList.toggle('hidden');
    }
}
if (crossImage){
    crossImage.addEventListener("click", function(){
        groupModal.classList.toggle('hidden');
        fullscreen.classList.toggle("hidden");
    })
}

// $(document).ready(
//     function(){
//         $(".delete-user-from-cookie").each(function(){
//             let id = this.id
//             $(this).on("click", function(){
//                 console.log("asdas")
//                 $.ajax({
//                     url: id,
//                     type: 'get',
//                     success: function(){
//                         console.log("success ajax")
//                     }
//                 })
//             })
//         })
//     }
// )