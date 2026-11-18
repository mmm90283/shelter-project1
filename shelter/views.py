from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Animal
from .forms import AdoptionForm


def home(request):
    animals = Animal.objects.filter(is_adopted=False)[:3]
    return render(request, 'home.html', {'animals': animals})


def about(request):
    return render(request, 'about.html')


def animals_view(request):
    all_animals = Animal.objects.all()
    return render(request, 'animals.html', {'animals': all_animals})


def rules(request):
    return render(request, 'rules.html')


def contacts(request):
    if request.method == 'POST':
        form = AdoptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо! Ваша заявка отправлена.')
            return redirect('contacts')
    else:
        form = AdoptionForm()
    return render(request, 'contacts.html', {'form': form})