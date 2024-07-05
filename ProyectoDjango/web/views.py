from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from .forms import RegistroForm, LoginForm

# Create your views here.
def Index(request):
    context={}
    return render(request, 'web/Index.html', context)

def Rosas(request):
    context={}
    return render(request, 'web/Rosas.html', context)

def Claveles(request):
    context={}
    return render(request, 'web/Claveles.html', context)

def Tulipanes(request):
    context={}
    return render(request, 'web/Tulipanes.html', context)

def Girasoles(request):
    context={}
    return render(request, 'web/Girasoles.html', context)

def Gerbera(request):
    context={}
    return render(request, 'web/Gerbera.html', context)

def Macetero(request):
    context={}
    return render(request, 'web/Macetero.html', context)

def Arbustos(request):
    context={}
    return render(request, 'web/Arbustos.html', context)

def Tierra(request):
    context={}
    return render(request, 'web/Tierra.html', context)

def Plantas(request):
    context={}
    return render(request, 'web/Plantas.html', context)

def Abono(request):
    context={}
    return render(request, 'web/Abono.html', context)

def Registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Ya se registró!')  # Mensaje de éxito
            return redirect('Login/')  # Redirige a la página Login o donde desees
    else:
        form = RegistroForm()
    
    return render(request, 'web/Registro.html', {'form': form})

def Login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Ya se registró!')  # Mensaje de éxito
            return redirect('Index/')  # Redirige a la página de Index o donde desees
    else:
        form = LoginForm()
    
    return render(request, 'web/Login.html', {'form': form})


#CRUD
def crud(request):
    web = Usuario.objects.all()
    context = {"web" : web}
    return render(request, 'web/Usuarios_lista.html', context)

def listadoSQL(request, codigo):
    web = Usuario.objects.raw('SELECT * FROM web_usuario')
    print(web)
    context={"web":web}
    return render(request, 'web/listadoSQL.html', context)

def UsuariosAdd(request):
    if request.method is not "POST":
        web = Usuario.objects.all()
        context={"web": web}
        return render (request, 'web/Usuarios_add.html', context)
    else:    
        Nombre=request.POST["Nombre"]
        Apellido=request.POST["Apellido"]
        Gmail=request.POST["Gmail"]
        Contraseña=request.POST["Contraseña"]

        obj=Usuario.objects.create(Nombre=Nombre,
                                    Apellido=Apellido,
                                    Gmail=Gmail,
                                    Contraseña=Contraseña)
        obj.save()
        context={'mensaje':"Ok, datos grabados..."}
        return render(request, 'web/Usuarios_add.html', context)

def Usuarios_del(request,pk):
    context={}
    try:
        usuario = Usuario.objects.get(nombre=pk)

        usuario.delete()
        mensaje = "Bien, Datos Eliminados..."
        web = Usuario.objects.all()
        context = {'web' : web, 'mensaje' : mensaje}
        return render(request, 'web/Usuarios_lista.html', context)
    except:
        mensaje="Error, Nombre no Existente"
        web = Usuario.objects.all()
        context = {'web' : web, 'mensaje' : mensaje}
        return render(request, 'web/Usuarios_lista.html', context)

def Usuarios_findEdit(request,pk):
    if pk != "":
        usuario=Usuario.objects.get(nombre=pk)
        web = Usuario.objects.all()
        context={'web' : web}
        if usuario:
            return render(request, 'web/Usuarios_edit.html', context)
        else:
            context={'mensaje': "Error, Nombre no Existente"}
            return render(request, 'web/Usuarios_edit.html', context)
def UsuarioUpdate (request):
    if request.method == "POST":
        Nombre=request.POST["Nombre"]
        Apellido=request.POST["Apellido"]
        Gmail=request.POST["Gmail"]
        Contraseña=request.POST["Contraseña"]

        usuario = Usuario()
        usuario.nombre=Nombre
        usuario.apellido=Apellido
        usuario.gmail=Gmail
        usuario.contraseña.Contraseña
        usuario.save()

        web = Usuario.objects.all()
        context={'mensaje':"Ok, datos actualizados...", 'web': web}
        return render (request, 'web/Usarios_edit.html', context)
    else:
        web= Usuario.objects.all() 
        context={'web': web}
        return render(request, 'web/Usarios_edit.html', context)
