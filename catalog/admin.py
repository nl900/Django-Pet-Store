from django.contrib import admin

from catalog.models import Animal, Pet, Breeder
# Register your models here.

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_select_related = ('animal', 'breeder',)
    list_display = ('id', 'animal')

    class Meta:
        model = Pet

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_select_related = ('parent',)
    list_display = ('name', 'parent', )
    class Meta:
        model = Animal

@admin.register(Breeder)
class BreederAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
