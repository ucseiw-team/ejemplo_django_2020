from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=200)
    fecha = models.DateTimeField()
    archivada = models.BooleanField(default=False)
    denuncias = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, null=True, blank=True,
                                  on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class FotoNoticia(models.Model):
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="fotos_noticias")
