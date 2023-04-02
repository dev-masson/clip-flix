from django.contrib import admin
from .models import Clip, Episode, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

campos = list(UserAdmin.fieldsets)
campos.append(
    ("Historico", {"fields": ("clip_seen",)})

)
UserAdmin.fieldsets = tuple(campos)

admin.site.register(Clip)
admin.site.register(Episode)
admin.site.register(User, UserAdmin)
