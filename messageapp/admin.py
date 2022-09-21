from django.contrib import admin

from .models import Mailing, Client, Text_message


admin.site.register(Mailing)
admin.site.register(Client)
admin.site.register(Text_message)
