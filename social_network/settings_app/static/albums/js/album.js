let createAlbumButton = document.querySelector("#createAlbumButton")
let windowAddAlbum = document.querySelector("#windowAddAlbum")
let centerAddAlbum = document.querySelector("#centerAddAlbum")
let crossButton = document.querySelector("#crossButton")


createAlbumButton.addEventListener('click', ()=>{
    centerAddAlbum.classList.toggle('hidden')
    windowAddAlbum.classList.toggle('hidden')
})

crossButton.addEventListener('click', ()=>{
    centerAddAlbum.classList.toggle('hidden')
    windowAddAlbum.classList.toggle('hidden')
})