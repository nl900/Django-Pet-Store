from django.contrib import admin

from catalog.models import Animal, Pet, Breeder
# Register your models here.

admin.site.register(Animal)
admin.site.register(Pet)
admin.site.register(Breeder)


class PetAdmin(admin.ModelAdmin):
    list_select_related = ('animal', 'breeder',)
    class Meta:
        model = Pet

class AnimalAdmin(admin.ModelAdmin):
    list_select_related = ('parent',)
    list_display = ('name', 'parent', )
    class Meta:
        model = Animal
