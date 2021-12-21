from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Categoria)
admin.site.register(Altapost)
admin.site.register(Comentario)
admin.site.register(ComentariosObj)
admin.site.register(Objetivo)