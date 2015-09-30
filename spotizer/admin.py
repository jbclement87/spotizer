from django.contrib import admin
from .models import Style, Artiste, Album, Morceau
# Register your models here.


admin.site.register(Artiste)
admin.site.register(Style)
admin.site.register(Album)
admin.site.register(Morceau)