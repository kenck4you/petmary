from django.shortcuts import render, redirect

from .models import Pet
from .forms import PetForm

from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'pets/index.html')

@login_required
def create_pet(request):
    if request.method != 'POST':
        form = PetForm()
    else:
        form = PetForm(data=request.POST)
        if form.is_valid():
            pet = form.save()
            pet.owners.add(request.user)
            return redirect('pets:pet', pet_id = pet.id)
        
    context = {'form': form}
    return render(request, 'pets/create_pet.html', context)
        
def pet(request, pet_id):
    pet = Pet.objects.get(id=pet_id)

    context = {'pet': pet}
    return render(request, 'pets/pet.html', context)