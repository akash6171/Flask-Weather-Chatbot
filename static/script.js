async function sendMessage() {
  const input = document.getElementById("msg");
  const chatBox = document.getElementById("chat-box");
  const userMessage = input.value.trim();

  if (!userMessage) return;

  // Add user message
  addMessage(userMessage, "user");

  // Clear input
  input.value = "";

  // Send to backend
  const res = await fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userMessage })
  });

  const data = await res.json();

  // Add bot reply
  addMessage(data.reply, "bot");
}

function addMessage(text, sender) {
  const chatBox = document.getElementById("chat-box");
  const msgDiv = document.createElement("div");
  msgDiv.classList.add("message", sender);
  msgDiv.innerText = text;
  chatBox.appendChild(msgDiv);

  // Scroll to bottom
  chatBox.scrollTop = chatBox.scrollHeight;
}

// Allow "Enter" key to send message
document.getElementById("msg").addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    sendMessage();
  }
});
