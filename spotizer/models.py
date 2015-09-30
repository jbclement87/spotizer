from django.db import models



class Style(models.Model):
    style = models.CharField(max_length=200)
    def __str__(self):
        return self.style


class Artiste(models.Model):
    nom = models.CharField(max_length=200)
    style = models.ForeignKey(Style)
    image = models.ImageField(upload_to='media/img')
    def __str__(self):
        return self.nom


class Album(models.Model):
    artiste = models.ForeignKey(Artiste)
    nom = models.CharField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='media/img')
    def __str__(self):
        return self.nom


class Morceau(models.Model):
    album = models.ForeignKey(Album)
    nom = models.CharField(max_length=200)
    file = models.FileField(upload_to='media/mp3')
    def __str__(self):
        return self.nom

    class Meta:
        verbose_name_plural = "morceaux"
