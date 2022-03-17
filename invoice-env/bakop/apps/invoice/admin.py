from django.contrib import admin
from .models import Invoice, Item

admin.site.register(Item)
admin.site.register(Invoice)

# Register your models here.
