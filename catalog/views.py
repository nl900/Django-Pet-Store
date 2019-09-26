from django.shortcuts import render
from django.views import generic

from catalog.models import Animal, Pet, Breeder

# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_animal = Animal.objects.all().count()
    
    # Available (status = 'a')
    pet_available = Pet.objects.filter(status__exact='a').count()
    
    # The 'all()' is implied by default.    
    num_breeder = Breeder.objects.count()
    
    context = {
        'num_animal': num_animal,
        'num_pet_available': pet_available ,
        'num_breeder': num_breeder,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

class PetListView(generic.ListView):
    model = Pet

class PetDetailView(generic.DetailView):
    model = Pet

class BreederListView(generic.ListView):
    model = Breeder

class BreederDetailView(generic.DetailView):
    model = Breeder
