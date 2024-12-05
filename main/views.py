from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, BookingForm
from .models import Service, Gallery, Testimonial, TeamMember, SiteSettings, Promotion

def get_common_context():
    try:
        site_settings = SiteSettings.objects.first()
    except SiteSettings.DoesNotExist:
        site_settings = None
    return {'site_settings': site_settings}

def home(request):
    context = get_common_context()
    context.update({
        'services': Service.objects.filter(is_active=True).order_by('order')[:6],
        'testimonials': Testimonial.objects.filter(is_active=True).order_by('order')[:6],
        'promotions': Promotion.objects.filter(is_active=True).order_by('order'),
    })
    return render(request, 'main/home.html', context)

def services(request):
    context = get_common_context()
    context.update({
        'services': Service.objects.filter(is_active=True).order_by('order'),
    })
    return render(request, 'main/services.html', context)

def gallery(request):
    context = {
        'gallery_items': Gallery.objects.filter(is_active=True).order_by('order'),
        'categories': Gallery.CATEGORY_CHOICES,
    }
    return render(request, 'main/gallery.html', context)

def about(request):
    context = {
        'site_settings': SiteSettings.objects.first(),
        'team_members': TeamMember.objects.filter(is_active=True).order_by('order'),
    }
    return render(request, 'main/about.html', context)

def contact(request):
    context = get_common_context()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data here
            messages.success(request, 'Votre message a été envoyé avec succès!')
            return redirect('contact')
    else:
        form = ContactForm()
    context['form'] = form
    return render(request, 'main/contact.html', context)

def booking(request):
    context = get_common_context()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre réservation a été effectuée avec succès!')
            return redirect('booking')
    else:
        form = BookingForm()
    context['form'] = form
    return render(request, 'main/booking.html', context)
