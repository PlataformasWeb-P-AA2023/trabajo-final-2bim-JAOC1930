from django.db import models

# Create your models here.
class Barrio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
            return "%s" % (self.nombre)

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.IntegerField()

    def __str__(self):
            return "%s %s %d" % (self.nombre,
                    self.apellido, self.cedula)

class LocalComida(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='propietario_Comida')
    direccion = models.CharField(max_length=30)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE, related_name='barrio_Comida')
    tipo_comida = models.CharField(max_length=30)
    ventas_proyectadas_mes = models.FloatField()

    def obtenerVentas(self):
        var = self.ventas_proyectadas_mes
        valorTotal = var * 0.8
        return valorTotal


    def __str__(self):
            return "%s %s %s %s %.2f %.2f" % (self.propietario,
                    self.direccion, self.barrio, self.tipo_comida, 
                    self.ventas_proyectadas_mes, self.pago_permiso)
                    

class LocalRepuestos(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=30)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)
    valor_total_mercaderia = models.FloatField()

    def obtenerVentas2(self):
        var = self.valor_total_mercaderia
        valorTotal = var * 0.001
        return valorTotal

    def __str__(self):
            return "%s %s %s %.2f %.2f" % (self.propietario,
                    self.direccion, self.barrio, self.valor_total_mercaderia, 
                    self.valor_pago_permiso)