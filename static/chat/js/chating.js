$(document).ready(function () {
  $("#inputForm").on("submit", function (event) {
    event.preventDefault();

    // Get the input value
    var inputField = $(this).find('input[type="text"]');
    let message = inputField.val().trim();

    if (!message.length) {
      inputField.val("");
      inputField.focus();
      return;
    }

    // Create a new owner message
    let userPic = $(".user-profile").attr("src");
    var newMessage = `
      <div class="chat-msg owner">
          <div class="chat-msg-profile">
              <img class="chat-msg-img" src="${userPic}" alt="" />
              <div class="chat-msg-date">Message sent just now</div>
          </div>
          <div class="chat-msg-content">
              <div class="chat-msg-text">
                  ${message}
              </div>
          </div>
      </div>
    `;

    // Append the new message to the chat area
    $(".chat-area-main").append(newMessage);

    // Clear the input field
    inputField.val("");
    var chatBotPicSrc = $("#ChatBotPic").attr("src");

    // Send the input value to the server using jQuery's AJAX
    fetch("", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({
        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
        message: message,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        const response = data.response;
        var newMessage = `
      <div class="chat-msg ">
          <div class="chat-msg-profile">
              <img class="chat-msg-img" src="${chatBotPicSrc}" alt="" />
              <div class="chat-msg-date">Message sent just now</div>
          </div>
          <div class="chat-msg-content">
              <div class="chat-msg-text">
                  ${response}
              </div>
          </div>
      </div>
    `;

        // Append the new message to the chat area
        $(".chat-area-main").append(newMessage);
      });
  });
});
