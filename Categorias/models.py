from django.db import models

# Create your models here.


class Restaurantes (models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    horario = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=120)
    lat = models.CharField(max_length=20)
    log = models.CharField(max_length=20)
    img_logo = models.CharField(max_length=200)
    img_banner = models.CharField(max_length=200)
    img1 = models.CharField(max_length=200)
    img2 = models.CharField(max_length=200)
    img3 = models.CharField(max_length=200)
    img4 = models.CharField(max_length=200)
    img5 = models.CharField(max_length=200)
    #categoria = models.ForeignKey(Categoria)

    class Meta:
        ordering = ('name',)


class Esteticas (models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    horario = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=120)
    lat = models.CharField(max_length=20)
    log = models.CharField(max_length=20)
    img_logo = models.CharField(max_length=200)
    img_banner = models.CharField(max_length=200)
    img1 = models.CharField(max_length=200)
    img2 = models.CharField(max_length=200)
    img3 = models.CharField(max_length=200)
    img4 = models.CharField(max_length=200)
    img5 = models.CharField(max_length=200)
    #categoria = models.ForeignKey(Categoria)

    class Meta:
        ordering = ('name',)

class Hoteles (models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    horario = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=120)
    lat = models.CharField(max_length=20)
    log = models.CharField(max_length=20)
    img_logo = models.CharField(max_length=200)
    img_banner = models.CharField(max_length=200)
    img1 = models.CharField(max_length=200)
    img2 = models.CharField(max_length=200)
    img3 = models.CharField(max_length=200)
    img4 = models.CharField(max_length=200)
    img5 = models.CharField(max_length=200)
    #categoria = models.ForeignKey(Categoria)

    class Meta:
        ordering = ('name',)


class Veterinarias (models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    description = models.CharField(max_length=120)
    horario = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=120)
    lat = models.CharField(max_length=20)
    log = models.CharField(max_length=20)
    img_logo = models.CharField(max_length=200)
    img_banner = models.CharField(max_length=200)
    img1 = models.CharField(max_length=200)
    img2 = models.CharField(max_length=200)
    img3 = models.CharField(max_length=200)
    img4 = models.CharField(max_length=200)
    img5 = models.CharField(max_length=200)
    #categoria = models.ForeignKey(Categoria)

    class Meta:
        ordering = ('name',)




        

