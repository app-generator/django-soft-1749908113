# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Producto(models.Model):

    #__Producto_FIELDS__
    nombre = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(max_length=255, null=True, blank=True)

    #__Producto_FIELDS__END

    class Meta:
        verbose_name        = _("Producto")
        verbose_name_plural = _("Producto")


class Partners(models.Model):

    #__Partners_FIELDS__
    tipo_documento = models.CharField(max_length=255, null=True, blank=True)
    numero_documento = models.CharField(max_length=255, null=True, blank=True)
    contribuyente = models.BooleanField()
    correo = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    celular = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    ciudades = models.ForeignKey(ciudades, on_delete=models.CASCADE)

    #__Partners_FIELDS__END

    class Meta:
        verbose_name        = _("Partners")
        verbose_name_plural = _("Partners")


class Country(models.Model):

    #__Country_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Country_FIELDS__END

    class Meta:
        verbose_name        = _("Country")
        verbose_name_plural = _("Country")


class Departamentos(models.Model):

    #__Departamentos_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Departamentos_FIELDS__END

    class Meta:
        verbose_name        = _("Departamentos")
        verbose_name_plural = _("Departamentos")


class Distritos(models.Model):

    #__Distritos_FIELDS__
    departamento = models.ForeignKey(departamentos, on_delete=models.CASCADE)

    #__Distritos_FIELDS__END

    class Meta:
        verbose_name        = _("Distritos")
        verbose_name_plural = _("Distritos")


class Ciudades(models.Model):

    #__Ciudades_FIELDS__
    distrito = models.ForeignKey(distritos, on_delete=models.CASCADE)

    #__Ciudades_FIELDS__END

    class Meta:
        verbose_name        = _("Ciudades")
        verbose_name_plural = _("Ciudades")


class Facturas(models.Model):

    #__Facturas_FIELDS__
    numero_factura = models.CharField(max_length=255, null=True, blank=True)
    partner = models.ForeignKey(partners, on_delete=models.CASCADE)
    monto = models.IntegerField(null=True, blank=True)
    fecha = models.DateTimeField(blank=True, null=True, default=timezone.now)
    condicion = models.CharField(max_length=255, null=True, blank=True)
    moneda = models.ForeignKey(monedas, on_delete=models.CASCADE)

    #__Facturas_FIELDS__END

    class Meta:
        verbose_name        = _("Facturas")
        verbose_name_plural = _("Facturas")


class Monedas(models.Model):

    #__Monedas_FIELDS__
    descripcion = models.CharField(max_length=255, null=True, blank=True)

    #__Monedas_FIELDS__END

    class Meta:
        verbose_name        = _("Monedas")
        verbose_name_plural = _("Monedas")


class Lineas_Facturas(models.Model):

    #__Lineas_Facturas_FIELDS__
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=True, blank=True)
    precio = models.IntegerField(null=True, blank=True)
    factura = models.ForeignKey(facturas, on_delete=models.CASCADE)
    iva = models.IntegerField(null=True, blank=True)

    #__Lineas_Facturas_FIELDS__END

    class Meta:
        verbose_name        = _("Lineas_Facturas")
        verbose_name_plural = _("Lineas_Facturas")



#__MODELS__END
