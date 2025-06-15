const chatGroup = document.getElementById("chatGroupId").value

const socketUrl = `ws://${window.location.host}/chats/all_chats/${chatGroup}`;

const socket = new WebSocket(socketUrl);

const messages = document.getElementById("messages")
const form = document.getElementById("form")

form.addEventListener("submit", (event) => {
    // 
    event.preventDefault()
    // 
    let message = document.getElementById("id_message").value
    // 
    socket.send(JSON.stringify({"message": message}))
    // 
    form.reset()
})
socket.addEventListener('message', function(event){
    const messageObject = JSON.parse(event.data)
    const messageElem = document.createElement('p')
    messageElem.class = "one-message"
    messageElem.textContent = messageObject["message"]
    messages.scrollTop = messages.scrollHeight
    messages.append(messageElem)

})


        
