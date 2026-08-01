/* chatbot.js
   Floating chat widget that talks to /api/chat.
   Drop this file into static/ and include it in templates/index.html:
   <script src="{{ url_for('static', filename='chatbot.js') }}"></script>
*/

(function () {
  const toggleBtn = document.getElementById("chat-toggle-btn");
  const panel = document.getElementById("chat-panel");
  const closeBtn = document.getElementById("chat-close-btn");
  const form = document.getElementById("chat-form");
  const input = document.getElementById("chat-input");
  const messagesEl = document.getElementById("chat-messages");
  const sendBtn = document.getElementById("chat-send-btn");

  if (!toggleBtn || !panel || !form) return; // widget markup not present yet

  toggleBtn.addEventListener("click", () => {
    panel.classList.toggle("open");
    if (panel.classList.contains("open")) input.focus();
  });

  closeBtn.addEventListener("click", () => panel.classList.remove("open"));

  function appendMessage(text, sender) {
    const bubble = document.createElement("div");
    bubble.className = `chat-bubble ${sender}`;
    bubble.textContent = text;
    messagesEl.appendChild(bubble);
    messagesEl.scrollTop = messagesEl.scrollHeight;
    return bubble;
  }

  function setLoading(isLoading) {
    sendBtn.disabled = isLoading;
    input.disabled = isLoading;
  }

  async function sendMessage(message) {
    appendMessage(message, "user");
    const typingBubble = appendMessage("...", "bot typing");
    setLoading(true);

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message }),
      });
      const data = await res.json();
      typingBubble.remove();

      if (!res.ok) {
        appendMessage(data.error || "Something went wrong. Please try again.", "bot error");
        return;
      }
      appendMessage(data.reply, "bot");
    } catch (err) {
      typingBubble.remove();
      appendMessage("Connection issue — please try again in a moment.", "bot error");
    } finally {
      setLoading(false);
    }
  }

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const message = input.value.trim();
    if (!message) return;
    input.value = "";
    sendMessage(message);
  });

  // Greet on first open
  let greeted = false;
  toggleBtn.addEventListener("click", () => {
    if (!greeted && panel.classList.contains("open")) {
      appendMessage(
        "Hi! I'm Quamrul's portfolio assistant. Ask me about his projects, skills, experience, or education.",
        "bot"
      );
      greeted = true;
    }
  });
})();
