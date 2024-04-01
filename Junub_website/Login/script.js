document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
  
    form.addEventListener("submit", function(event) {
      event.preventDefault();
      if (validateForm()) {
        // Perform actions upon successful form submission
        alert("Login successful!");
      }
    });
  
    function validateForm() {
      const username = document.querySelector("input[type='text']").value;
      const password = document.querySelector("input[type='password']").value;
  
      if (username.trim() === "" || password.trim() === "") {
        alert("Please fill in all fields");
        return false;
      }
  
      return true;
    }
  });
  