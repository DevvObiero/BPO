const chatbox =
document.getElementById('chat');
const userInput =
document.getElementById('user-input');
const sendBtn =
document.getElementById('send-btn');

sendBtn.addEventListener('click', () => {
    const message =
    userInput.value.trim();
    if (message === '') return;

    appendMessage('You', message);
    userInput.value = '';

    fetch('http://127.0.0.1:5000/chat', {
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        body:
    JSON.stringify({message: message})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.reply) {
        appendMessage('Bot', data.reply);
        } else {
            appendMessage('Bot', 'No reply received from the server.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        appendMessage('Bot', 'An error occured...');
    });
});

function appendMessage(sender, message) {
    const div =
    document.createElement('div');
    div.classList.add('message');
    div.innerHTML = `<span class="${sender.toLowerCase()}">${sender}:</span> ${message}`;
    chatbox.appendChild(div);
    chatbox.scrollTop =
    chatbox.scrollHeight;
}

userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter")
sendBtn.click();
});
