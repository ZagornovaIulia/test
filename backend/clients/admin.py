from clients.models import Client
from django.contrib import admin


class ClientAdmin(admin.ModelAdmin):
    pass


admin.site.register(Client, ClientAdmin)
