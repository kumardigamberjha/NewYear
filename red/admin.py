from django.contrib import admin

# Register your models here.
from .models import FormModel, SaveImage

admin.site.register(FormModel)
admin.site.register(SaveImage)
