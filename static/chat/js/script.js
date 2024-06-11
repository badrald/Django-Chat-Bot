const toggleButton = document.querySelector(".dark-light");
const colors = document.querySelectorAll(".color");

colors.forEach((color) => {
  color.addEventListener("click", (e) => {
    colors.forEach((c) => c.classList.remove("selected"));
    const theme = color.getAttribute("data-color");
    document.body.setAttribute("data-theme", theme);
    color.classList.add("selected");
  });
});

toggleButton.addEventListener("click", () => {
  document.body.classList.toggle("dark-mode");
});

document.addEventListener("DOMContentLoaded", function () {
  const toggleButton = document.getElementById("toggle-button");
  const conversationArea = document.querySelector(".conversation-area");
  const chatArea = document.querySelector(".chat-area");
  const overlay = document.querySelector(".overlay");

  toggleButton.addEventListener("click", function () {
    conversationArea.classList.toggle("open");
    chatArea.classList.toggle("shrink");
    overlay.classList.toggle("show");
    toggleButton.classList.toggle("open");
  });

  overlay.addEventListener("click", function () {
    conversationArea.classList.remove("open");
    chatArea.classList.remove("shrink");
    overlay.classList.remove("show");
    toggleButton.classList.remove("open");
  });
});
