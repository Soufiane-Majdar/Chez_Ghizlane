from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, BookingForm

# Create your views here.

def home(request):
    return render(request, 'main/home.html')

def services(request):
    services_list = [
        {
            'name': 'Coiffure',
            'description': 'Coupes, brushings, et coiffures pour toutes occasions',
            'price': 'À partir de 150 MAD'
        },
        {
            'name': 'Lissage',
            'description': 'Lissage brésilien, japonais, et traitements professionnels',
            'price': 'À partir de 500 MAD'
        },
        {
            'name': 'Soins Visage',
            'description': 'Nettoyage, masques, et soins personnalisés',
            'price': 'À partir de 200 MAD'
        }
    ]
    return render(request, 'main/services.html', {'services': services_list})

def gallery(request):
    return render(request, 'main/gallery.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Send email
            send_mail(
                f'Nouveau message de {name}',
                message,
                email,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            
            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'main/contact.html', {'form': form})

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # Process the booking
            form.save()
            messages.success(request, 'Votre rendez-vous a été réservé avec succès!')
            return redirect('booking')
    else:
        form = BookingForm()
    
    return render(request, 'main/booking.html', {'form': form})
