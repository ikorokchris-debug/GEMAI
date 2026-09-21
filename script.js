const form = document.getElementById("chatForm");

const input = document.getElementById("messageInput");

const chat = document.getElementById("chat");

const typing = document.getElementById("typing");


form.addEventListener("submit", async function(event) {

    event.preventDefault();

    const message = input.value.trim();

    if (!message) {
        return;
    }


    addMessage(message, "user");


    input.value = "";

    typing.style.display = "block";


    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });


        const data = await response.json();


        typing.style.display = "none";


        if (data.reply) {

            addMessage(data.reply, "gem");

        } else {

            addMessage(
                "Sorry, something went wrong.",
                "gem"
            );

        }


    } catch (error) {

        typing.style.display = "none";

        addMessage(
            "I couldn't connect to the server.",
            "gem"
        );

        console.error(error);

    }

});


function addMessage(text, sender) {

    const message = document.createElement("div");

    message.className =
        sender === "user"
        ? "message user-message"
        : "message gem-message";


    message.innerHTML = `

        <div class="avatar">
            ${sender === "user" ? "U" : "G"}
        </div>

        <div class="bubble">
            ${escapeHTML(text)}
        </div>

    `;


    chat.appendChild(message);

    chat.scrollTop = chat.scrollHeight;

}


function escapeHTML(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;

}