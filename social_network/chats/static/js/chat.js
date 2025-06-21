const chatGroup = document.getElementById("chatGroupId").value

const socketUrl = `ws://${window.location.host}/chats/all_chats/${chatGroup}`;

const socket = new WebSocket(socketUrl);

const messages = document.getElementById("messages");
const form = document.getElementById("form");
const dateTime = document.querySelectorAll(".message-time");
for (let time of dateTime){
    let dateAndTime = new Date(time.textContent);
    let dateAndTimeLocal = dateAndTime.toLocaleString([], { hour: '2-digit', minute: '2-digit' });
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
    const messageWithAvatar = document.createElement('div');
    
    const messageObject = JSON.parse(event.data);
    const messageElem = document.createElement('div');
    messageElem.classList.add("one-message");
    const username  = document.createElement('p');  
    const messageAndTime = document.createElement('div');
    const avatar = document.createElement('img');
    const hiddenInputId = document.querySelector(".input-name").value;
    if (Number(hiddenInputId) !== messageObject['user_id']){
        username.textContent = `${messageObject['username']}`;
        username.classList.add('message-author');
        messageElem.append(username);
        messageElem.classList.add("author-people");
        for (let count = 0; count < messageObject["all_avatars"].length; count ++){
            let ProfileAvatar = messageObject["all_avatars"][count]
            let profileId = messageObject["profile_id"]
            if (ProfileAvatar.fields.profile == profileId){
                avatar.classList.add("avatar-people");
                avatar.src = "/media/" + ProfileAvatar.fields.image
                messageWithAvatar.append(avatar)
                messageWithAvatar.classList.add('message-with-avatar')
                messageWithAvatar.classList.add('author-people-message')
            }
    }
    }
    else{ 
        messageElem.classList.add("author-me")
    }

    const message = document.createElement('p')
    message.textContent = `${messageObject['message']}`
    messageAndTime.append(message)
    const time = document.createElement('p')
    messageAndTime.classList.add("message-and-time")
    time.classList.add('message-time')
    let dateAndTime = new Date(messageObject['date_time']);
    let dateAndTimeLocal = dateAndTime.toLocaleString([], { hour: '2-digit', minute: '2-digit' });
    time.textContent = dateAndTimeLocal
    messageAndTime.append(time)

    message.classList.add("message-content")
    messageElem.append(messageAndTime)
    messageWithAvatar.append(messageElem)   
    messages.append(messageWithAvatar)
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
