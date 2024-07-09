document.getElementById("formulario").addEventListener("submit", (event) => {
  event.preventDefault();

  // Validar nombre
  let entradaNombre = document.getElementById("nombre");
  let errorNombre = document.getElementById("errorNombre");
  if (entradaNombre.value.trim() === "") {
    errorNombre.textContent = "Por favor ingresa tu Nombre";
    errorNombre.classList.add("error-message");
  } else {
    errorNombre.textContent = "";
    errorNombre.classList.remove("error-message");
  }

  // Validar apellido
  let entradaApellido = document.getElementById("apellido");
  let apellidoError = document.getElementById("apellidoError");
  if (entradaApellido.value.trim() === "") {
    apellidoError.textContent = "Por favor ingresa tu Apellido";
    apellidoError.classList.add("error-message");
  } else {
    apellidoError.textContent = "";
    apellidoError.classList.remove("error-message");
  }

  // Validar correo
  let emailEntrada = document.getElementById("email");
  let emailError = document.getElementById("emailError");
  let emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Patrón de validación
  if (!emailPattern.test(emailEntrada.value.trim())) {
    emailError.textContent = "Por favor ingresa un email válido";
    emailError.classList.add("error-message");
  } else {
    emailError.textContent = "";
    emailError.classList.remove("error-message");
  }
  // Validar teléfono
  let entradaTelefono = document.getElementById("telefono");
  let telefonoError = document.getElementById("telefonoError");
  let telefonoPattern = /^\d{3}\s\d{4}\s\d{4}$/; // Patrón de validación
  if (!telefonoPattern.test(entradaTelefono.value.trim())) {
    telefonoError.textContent = "Por favor ingresa un número de teléfono válido";
    telefonoError.classList.add("error-message");
  } else {
    telefonoError.textContent = "";
    telefonoError.classList.remove("error-message");
  }

  // Validar mensaje
  let entradaMensaje = document.getElementById("mensaje");
  let mensajeError = document.getElementById("mensajeError");
  if (entradaMensaje.value.trim() === "") {
    mensajeError.textContent = "Por favor ingresa tu mensaje y nos comunicaremos a la brevedad";
    mensajeError.classList.add("error-message");
  } else {
    mensajeError.textContent = "";
    mensajeError.classList.remove("error-message");
  }

  // Validar si todos los campos son válidos
  if (!errorNombre.textContent && !apellidoError.textContent && !emailError.textContent && !mensajeError.textContent) {
    alert("El formulario se ha enviado con éxito");
    document.getElementById("formulario").reset();
  }
});
