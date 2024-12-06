from django.contrib import admin
from .models import Livro, Autor, Editora, Emprestimo, Reserva, Usuario

admin.site.register(Livro)
admin.site.register(Autor)
admin.site.register(Editora)
admin.site.register(Emprestimo)
admin.site.register(Reserva)
admin.site.register(Usuario)