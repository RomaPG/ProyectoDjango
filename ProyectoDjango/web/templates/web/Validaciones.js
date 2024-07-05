<script>
$(document).ready(function(){
    $(".form-register").submit(function(event){
        var nombres = $("#ItNombre").val();
        var apellido = $("#ItApellido").val();
        var correo = $("#ItCorreo").val();
        var contraseña = $("#ItContraseña").val();
        
        if(!/^[a-zA-Z]+$/.test(nombres)) {
            $("#mensaje1").fadeIn();
            event.preventDefault();
        } else {
            $("#mensaje1").fadeOut();
        }

        if(!/^[a-zA-Z]+$/.test(apellido)) {
            $("#mensaje2").fadeIn();
            event.preventDefault();
        } else {
            $("#mensaje2").fadeOut();
        }

        if(!/\S+@\S+\.\S+/.test(correo)) {
            $("#mensaje3").fadeIn();
            event.preventDefault();
        } else {
            $("#mensaje3").fadeOut();
        }

        if(contraseña.length < 6) {
            $("#mensaje4").fadeIn();
            event.preventDefault();
        } else {
            $("#mensaje4").fadeOut();
        }
    })
});
</script>
