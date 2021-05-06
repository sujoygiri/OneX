from django.contrib import admin
from .models import EncrypteMessage,DecrypteMessage
# Register your models here.

admin.site.register(EncrypteMessage)
admin.site.register(DecrypteMessage)

