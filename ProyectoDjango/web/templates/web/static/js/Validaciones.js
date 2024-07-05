document.getElementById('registroForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var nombre = document.getElementById('nombre').value;
    var apellido = document.getElementById('apellido').value;
    var correo = document.getElementById('correo').value;
    var password1 = document.getElementById('password1').value;
    var password2 = document.getElementById('password2').value;
    var edad = parseInt(document.getElementById('edad').value);

    if (nombre.length < 3 || nombre.length > 20 || apellido.length < 3 || apellido.length > 20) {
        alert('El Nombre y el Apellido deben tener entre 3 y 20 caracteres.');
        return;
    }

    if (!correo.includes('@')) {
        alert('El correo electrónico debe contener "@" en el formato.');
        return;
    }
    if (password1 !== password2) {
        alert('Las contraseñas no coinciden.');
        return;
    }

    if (!/[a-z]/.test(password1) || !/[A-Z]/.test(password1) || !/\d/.test(password1)) {
        alert('La contraseña debe contener al menos una mayúscula, una minúscula y un número.');
        return;
    }

    alert('¡Registro exitoso!');

    // Reset the form fields
    document.getElementById('nombre').value = '';
    document.getElementById('apellido').value = '';
    document.getElementById('correo').value = '';
    document.getElementById('password1').value = '';
    document.getElementById('password2').value = '';
});
