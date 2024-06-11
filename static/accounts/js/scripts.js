$("#LogIn").on("submit", function (e) {
  e.preventDefault();

  const loginForm = new FormData(this);
  loginForm.append("csrfmiddlewaretoken", csrfToken); // Add CSRF token

  console.log(loginForm);
  $.ajax({
    type: "POST",
    url: "accounts/login/",
    data: loginForm,
    processData: false, // Important to set this to false
    contentType: false, // Important to set this to false
    success: function (data) {
      // Redirect to the homepage on successful login
      console.log(data);
      $(".statusMsg").removeClass("text-danger").addClass("text-info");
      $(".statusMsg").text(data.success);
      setTimeout(function () {
        window.location.reload();
      }, 2000);
    },
    error: function (xhr, status, error) {
      const errorMessage =
        xhr.responseJSON && xhr.responseJSON.error
          ? xhr.responseJSON.error
          : "There is an error with the connection";
      $(".statusMsg").removeClass("text-info").addClass("text-danger");
      $(".statusMsg").text(errorMessage);
      $("#LogIn input").val("");
    },
  });
});
$("#SignUp").on("submit", function (e) {
  e.preventDefault();

  const signupForm = new FormData(this);
  signupForm.append("csrfmiddlewaretoken", "{{ csrf_token }}"); // Add CSRF token
  $.ajax({
    type: "POST",
    url: "accounts/signIn/",
    data: signupForm,
    processData: false, // Important to set this to false
    contentType: false, // Important to set this to false
    success: function (data) {
      // Redirect to the homepage on successful login
      console.log(data);
      $(".statusMsg").removeClass("text-danger").addClass("text-info");
      $(".statusMsg").text(data.success);
      setTimeout(function () {
        window.location.reload();
      }, 2000);
    },
    error: function (xhr, status, error) {
      const errorMessage =
        xhr.responseJSON && xhr.responseJSON.error
          ? xhr.responseJSON.error
          : "There is an error with the connection";
      $(".statusMsg").removeClass("text-info").addClass("text-danger");
      $(".statusMsg").text(errorMessage);
      $("#signUp input").val("");
    },
  });
});
