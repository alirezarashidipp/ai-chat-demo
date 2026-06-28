async function sendMessage() {
    const message = document.getElementById("message").value;

    const response = document.getElementById("response");
    response.innerText = "Sending...";

    const result = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    const data = await result.json();
    response.innerText = data.reply;
}