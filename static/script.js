
// Set event listener after DOM content is fully loaded
document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("sendMessage").addEventListener("click", sendQuery);
});

document.getElementById("messageInput").addEventListener("keyup", (event) => {
  event.preventDefault();
  if (event.key === "Enter") {
    sendQuery();
  }
});

function sendQuery() {
  console.log("sendQuery called"); // This should log when you click the send button
  const userInput = document.getElementById("messageInput").value.trim();

  if (!userInput) {
    alert("Please enter your question");
    return;
  }

  appendMessage("user", userInput);
  // getResponse(userInput)
  //   .then((response) => {
  //     console.log(response); // This will log the whole response object
  //     if ('response' in response && response.response) {
  //       appendMessage("ai", response.response);
  //     } else if ('error' in response && response.error) {
  //       appendMessage("error", response.error);
  //     } else {
  //       appendMessage("error", "Sorry, an error occurred while fetching your answer.");
  //     }


    getResponse(userInput)
    .then((response) => {
      console.log(response); // This will log the whole response object
      if (typeof response.message === 'string') {
        appendMessage("ai", response.message);
      } else if ('response' in response && response.message ) {
        appendMessage("ai", response.message);
      } else if ('error' in response && response.error) {
        appendMessage("error", response.error);
      } else {
        appendMessage("error", "Sorry, an error occurred while fetching your answer.");
      }
    })



    .catch((error) => {
      console.error("Error during chat:", error);
      appendMessage("error", error.message || "Sorry, an error occurred while trying to send your message.");
    });

  document.getElementById("messageInput").value = ""; // Clear the input field after sending
}

function createChatBubble(sender, message) {
  const bubble = document.createElement("div");
  bubble.className = `message ${sender}`;
  bubble.innerText = message;
  return bubble;
}

function updateChat(sender, message) {
  const chatArea = document.getElementById("messageArea");
  const bubble = createChatBubble(sender, message);
  chatArea.appendChild(bubble);
  chatArea.scrollTop = chatArea.scrollHeight; // Scroll to the latest message
}

// Consolidated function for appending messages
function appendMessage(sender, message) {
  updateChat(sender, message);
}

// Modified function to integrate with the Ayurvedic GPT backend
function getResponse(query) {
  return fetch("/ask", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ prompt: query }),
  })
    .then((response) => {
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    });
}




