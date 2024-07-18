"use strict"

// // Prevent "enter" key to create models
// window.addEventListener("keydown", function (e) {
//   if (e.key == "Enter") {
//     e.preventDefault()
//   }
// })

// Close notification
const closeNotification = (event) => {
  const notificationElement = event.target.closest(".notification")

  if (event.target.classList.contains("icon-close")) {
    notificationElement.remove()
  }

  const notifContainer = document.querySelector(".messages-container")
  if (notifContainer.children.length === 0) {
    notifContainer.remove()
  }
}

document
  .querySelector(".messages-container")
  ?.addEventListener("click", (e) => {
    closeNotification(e)
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

// Confirm action before submitting
const confirmAction = function (elementClass, action) {
  const form = document.querySelector(`.${elementClass}`)

  form?.addEventListener("submit", function (e) {
    e.preventDefault()

    const confirmLogout = confirm(`Do you really want to ${action}?`)

    if (confirmLogout) {
      form.submit()
    }
  })
}

confirmAction("form-logout", "logout")
confirmAction("form-delete", "delete this contact")
