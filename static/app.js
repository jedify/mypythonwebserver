function loadData() {
    fetch("/api/message")
        .then((response) => response.json())
        .then((response) => {
            document.getElementById("message").innerText = response.message;
        });
}


function handleSubmit() {
    fetch("/", { method: 'POST', body: document.getElementById("inputmessage").value })
        .then((response) => { console.log(response); return response.text() })
        .then((message) => {
            document.getElementById("moremessage").append(createElement(message));
        });
}

function createElement(text) {
    var newMessage = document.createElement("div");
    newMessage.classList.add("tweet");
    newMessage.innerText = text;
    return newMessage;
}
