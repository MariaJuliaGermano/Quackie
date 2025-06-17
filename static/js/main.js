// Funcionalidades básicas do Quackie

document.addEventListener("DOMContentLoaded", () => {
  // Toggle de curtidas
  const likeButtons = document.querySelectorAll(".like-btn")
  likeButtons.forEach((button) => {
    button.addEventListener("click", function () {
      // Aqui você implementaria a lógica de curtir via AJAX
      const count = this.querySelector(".like-count")
      const currentCount = Number.parseInt(count.textContent)

      if (this.classList.contains("liked")) {
        count.textContent = currentCount - 1
        this.classList.remove("liked")
      } else {
        count.textContent = currentCount + 1
        this.classList.add("liked")
      }
    })
  })

  // Preview de imagem no upload
  const profilePictureInput = document.getElementById("profile_picture")
  if (profilePictureInput) {
    profilePictureInput.addEventListener("change", (e) => {
      const file = e.target.files[0]
      if (file) {
        const reader = new FileReader()
        reader.onload = (e) => {
          // Aqui você pode mostrar um preview da imagem
          console.log("Imagem selecionada:", file.name)
        }
        reader.readAsDataURL(file)
      }
    })
  }

  // Validação de formulários
  const forms = document.querySelectorAll("form")
  forms.forEach((form) => {
    form.addEventListener("submit", (e) => {
      const passwords = form.querySelectorAll('input[type="password"]')
      const confirmPassword = form.querySelector('input[name="confirm_password"], input[name="confirm_new_password"]')

      if (confirmPassword) {
        const password = form.querySelector('input[name="password"], input[name="new_password"]')
        if (password && password.value !== confirmPassword.value) {
          e.preventDefault()
          alert("As senhas não coincidem!")
        }
      }
    })
  })
})

// Função para formatar tempo (similar ao timesince do Django)
function timeAgo(date) {
  const now = new Date()
  const diffInSeconds = Math.floor((now - date) / 1000)

  if (diffInSeconds < 60) return `${diffInSeconds}s`
  if (diffInSeconds < 3600) return `${Math.floor(diffInSeconds / 60)}m`
  if (diffInSeconds < 86400) return `${Math.floor(diffInSeconds / 3600)}h`
  return `${Math.floor(diffInSeconds / 86400)}d`
}
