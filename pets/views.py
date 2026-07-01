from django.shortcuts import render, redirect

from .forms import PetForm

def index(request):
    return render(request, 'pets/index.html')

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
        