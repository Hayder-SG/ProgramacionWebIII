from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    correo = forms.EmailField(label="Correo", required=True)
class TiendaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True)
    direccion = forms.CharField(label="Direccion", required=True)

class CompraForm(forms.Form):
    fecha = forms.DateField(label="Fecha", required=True)
    monto = forms.IntegerField(label="Monto", required=True)
    id_cliente = forms.IntegerField(label="Id Cliente", required=True)
    id_tienda = forms.IntegerField(label="Id Tienda", required=True)