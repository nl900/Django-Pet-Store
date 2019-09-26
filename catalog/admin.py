from django.contrib import admin

from catalog.models import Animal, Pet, Breeder
# Register your models here.

admin.site.register(Animal)
admin.site.register(Pet)
admin.site.register(Breeder)
