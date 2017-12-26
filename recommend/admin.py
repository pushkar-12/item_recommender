from django.contrib import admin
from.models import User
from .models import snap,logo,movies

admin.site.register(User)
admin.site.register(snap)
admin.site.register(logo)
admin.site.register(movies)
# Register your models here.
