const chatGroup = document.getElementById("chatGroupId").value

const socketUrl = `ws://${window.location.host}/chats/all_chats/${chatGroup}`;

const socket = new WebSocket(socketUrl);

const messages = document.getElementById("messages");
const form = document.getElementById("form");
const dateTime = document.querySelectorAll(".message-time");
for (let time of dateTime){
    let dateAndTime = new Date(time.textContent);
    let dateAndTimeLocal = dateAndTime.toLocaleString();
    time.textContent = dateAndTimeLocal
}
form.addEventListener("submit", (event) => {
    // 
    event.preventDefault()
    // 
    let message = document.getElementById("id_message").value
    socket.send(JSON.stringify({"message": message}))
    // 
    form.reset()
})
socket.addEventListener('message', function(event){
    const messageObject = JSON.parse(event.data)
    const messageElem = document.createElement('div')
    messageElem.classList.add("one-message")
    const username  = document.createElement('p')   
    username.textContent = `${messageObject['username']}`
    username.classList.add('message-author')
    const message = document.createElement('p')
    message.textContent = `${messageObject['message']}`
    messageElem.append(message)
    message.classList.add("message-content")
    messageElem.append(username)
    messages.append(messageElem)
    const time = document.createElement('p')
    time.classList.add('message-time')
    let dateAndTime = new Date(messageObject['date_time']);
    let dateAndTimeLocal = dateAndTime.toLocaleString();
    time.textContent = dateAndTimeLocal
    messageElem.append(time)
    scrollMessagesToBottom()
})

window.addEventListener('load', ()=>{
    let divMessages = document.querySelector('.messages-class')
    divMessages.scrollTop = divMessages.scrollHeight;
})

function scrollMessagesToBottom(){
    let divMessages = document.querySelector('.messages-class')
    divMessages.scrollTop = divMessages.scrollHeight;
}
