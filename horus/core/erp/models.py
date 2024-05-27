from django.db import models
from datetime import datetime

from django.forms import model_to_dict

from core.erp.choices import tipo_Cliente


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null= True, blank=True, verbose_name="Descripcion")

    def __str__(self):
        return 'Nombre: {}'.format(self.name)
    
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class Client(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre')
    apellidoP = models.CharField(max_length=150, verbose_name='Apellido Paterno')
    apellidoM = models.CharField(max_length=150, verbose_name='Apellido Materno')  
    email = models.CharField(max_length=150, verbose_name='Correo Electronico')
    rfc = models.CharField(max_length=13, verbose_name='RFC')
    curp = models.CharField(max_length=18, verbose_name='CURP')
    telefono = models.PositiveIntegerField(verbose_name='Telefono')
    tipoCliente = models.CharField(max_length=20, choices=tipo_Cliente, blank=True, default='o',help_text='Book availability',)
    Cer = models.FileField(null=True)
    Key = models.FileField(null=True)
    passphrase = models.CharField(max_length=150,verbose_name='Passphrase')
    calle = models.CharField(max_length=150,verbose_name='Calle')
    numeroExterior = models.PositiveIntegerField(verbose_name='Numero Exterior')
    numeroInterior = models.PositiveIntegerField(verbose_name='Numero Interior')
    colonia = models.CharField(max_length=150,verbose_name='Colonia')
    localidad = models.CharField(max_length=150,verbose_name='Localidad')
    municipio = models.CharField(max_length=150,verbose_name='Municipio')
    estado = models.CharField(max_length=150,verbose_name='Estado')
    pais = models.CharField(max_length=150,verbose_name='pais')
    codigoPostal = models.CharField(max_length=150,verbose_name='Codigo Postal')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class Sale(models.Model):
    cli = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_joined = models.DateField(default=datetime.now)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.cli.names

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']


class DetSale(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cant = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        ordering = ['id']