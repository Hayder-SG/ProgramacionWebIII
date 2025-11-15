from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Tienda, Compra
from .forms import ClienteForm, CompraForm, TiendaForm
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# Create your views here.
def lista_clientes(request):
    clientes = Cliente.objects.all()  #select * from clientes
    return render(request, 'clientes/listar_clientes.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            Cliente.objects.create(
            nombre = form.cleaned_data['nombre'],
            email = form.cleaned_data['correo'] 
            )
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
        return render(request, 'clientes/nuevo_cliente.html',{'form': form})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente = id)
    cliente.delete()
    return redirect('lista_clientes')

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente = id)
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente.nombre = form.cleaned_data['nombre']
            cliente.email = form.cleaned_data['correo']
            cliente.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(initial={
            'nombre': cliente.nombre,
            'correo': cliente.email,
        })
        return render(request, 'clientes/actualizar_cliente.html', {'form':form})
    
# Tiendas

def listar_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request, 'tiendas/listar_tiendas.html', {'tiendas': tiendas})

def crear_tienda(request):
    if request.method == 'POST':
        form = TiendaForm(request.POST)
        if form.is_valid():
            Tienda.objects.create(
                nombre=form.cleaned_data['nombre'],
                direccion=form.cleaned_data['direccion']
            )
            return redirect('listar_tiendas')
    else:
        form = TiendaForm()
    return render(request, 'tiendas/nueva_tienda.html', {'form': form})

def actualizar_tienda(request, id):
    tienda = get_object_or_404(Tienda, id_tienda=id)
    if request.method == 'POST':
        tienda.nombre = request.POST.get('nombre')
        tienda.direccion = request.POST.get('direccion')
        tienda.save()
        return redirect('listar_tiendas')
    else:
        form = TiendaForm(initial={
            'nombre': tienda.nombre,
            'direccion': tienda.direccion
        })
        return render(request, 'tiendas/actualizar_tienda.html', {'form': form})

def eliminar_tienda(request, id):
    tienda = get_object_or_404(Tienda, id_tienda=id)
    tienda.delete()
    return redirect('listar_tiendas')


# Compras

def listar_compras(request):
    compras = Compra.objects.all()
    return render(request, 'compras/listar_compras.html', {'compras': compras})

def crear_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST)
        if form.is_valid():
            Compra.objects.create(
                fecha=form.cleaned_data['fecha'],
                monto=form.cleaned_data['monto'],
                id_cliente=form.cleaned_data['id_cliente'],
                id_tienda=form.cleaned_data['id_tienda']
            )
            return redirect('listar_compras')
    else:
        form = CompraForm()
    return render(request, 'compras/nueva_compra.html', {'form': form})

def actualizar_compra(request, id):
    compra = get_object_or_404(Compra, id_compra=id)
    if request.method == 'POST':
        compra.fecha = request.POST.get('fecha')
        compra.monto = request.POST.get('monto')
        compra.id_cliente_id = request.POST.get('id_cliente')
        compra.id_tienda_id = request.POST.get('id_tienda')
        compra.save()
        return redirect('listar_compras')
    else:
        form = CompraForm(initial={
            'fecha': compra.fecha,
            'monto': compra.monto,
            'id_cliente': compra.id_cliente,
            'id_tienda': compra.id_tienda
        })
        return render(request, 'compras/actualizar_compra.html', {'form': form})

def eliminar_compra(request, id):
    compra = get_object_or_404(Compra, id_compra=id)
    compra.delete()
    return redirect('listar_compras')


def presentacion(request):
    return render(request, 'presentacion.html')