"use strict"

// Prevent "enter" key to create models
window.addEventListener("keydown", function (e) {
  if (e.key == "Enter") {
    e.preventDefault()
  }
})

// Close notification
const notificationsContainer = document.querySelector(".messages-container")

notificationsContainer.addEventListener("click", function (e) {
  if (e.target.classList.contains("icon-close")) {
    const notificationElement = e.target.parentNode.parentNode
    notificationElement.remove()
  }
})

// Show/hide password
const passwordInputs = document.querySelectorAll(".password-input")

passwordInputs.forEach((el) => {
  el.addEventListener("click", function (e) {
    if (e.target.classList.contains("password-show-icon")) {
      const inputField = e.target.parentNode.querySelector(".field-input")

      if (inputField.type === "password") {
        inputField.type = "text"
        e.target.name = "eye-off-outline"
      } else {
        inputField.type = "password"
        e.target.name = "eye-outline"
      }
    }
  })
})

// Change color of field with error in form
const errors = document.querySelectorAll(".form-error")

if (errors) {
  errors.forEach((error) => {
    const inputLabel = error.parentElement.querySelector(".field-label")
    const inputEl = error.parentElement.querySelector(".field-input")

    inputLabel.style.color = "#f00"
    inputEl.style.border = "1px solid #f00"
    inputEl.style.color = "#f00"
  })
}

// Confirm to logout
const formLogout = document.querySelector(".form-logout")

formLogout.addEventListener("submit", function (e) {
  e.preventDefault()

  const confirmLogout = confirm("You really want to logout?")

  if (confirmLogout) {
    console.log("He confirmed")
    formLogout.submit()
  }
})
