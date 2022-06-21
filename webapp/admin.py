from django.contrib import admin
from .models import Post, Profile, Ticket

# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)

admin.site.register(Ticket)
#admin.site.register(Desayuno)
#admin.site.register(Almuerzo)
#admin.site.register(Lonche)