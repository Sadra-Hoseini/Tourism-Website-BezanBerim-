from django.contrib import admin
from .models import Tour



# super user informations : username = admin , email = admin@bezanberim.com , pass = 12345678

admin.site.register(Tour)