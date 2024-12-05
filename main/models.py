from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from cloudinary.models import CloudinaryField

class Booking(models.Model):
    SERVICES_CHOICES = [
        ('coiffure', _('Coiffure')),
        ('lissage', _('Lissage')),
        ('soins_visage', _('Soins Visage')),
    ]
    
    TIME_CHOICES = [
        ('10:30', '10:30'), ('11:00', '11:00'), ('11:30', '11:30'),
        ('12:00', '12:00'), ('12:30', '12:30'), ('13:00', '13:00'),
        ('13:30', '13:30'), ('14:00', '14:00'), ('14:30', '14:30'),
        ('15:00', '15:00'), ('15:30', '15:30'), ('16:00', '16:00'),
        ('16:30', '16:30'), ('17:00', '17:00'), ('17:30', '17:30'),
        ('18:00', '18:00'), ('18:30', '18:30'), ('19:00', '19:00'),
        ('19:30', '19:30'), ('20:00', '20:00'), ('20:30', '20:30'),
        ('21:00', '21:00')
    ]
    
    name = models.CharField(_('Nom'), max_length=100)
    email = models.EmailField(_('Email'))
    phone = models.CharField(_('Téléphone'), max_length=20)
    service = models.CharField(_('Service'), max_length=20, choices=SERVICES_CHOICES)
    date = models.DateField(_('Date'))
    time = models.CharField(_('Heure'), max_length=5, choices=TIME_CHOICES)
    notes = models.TextField(_('Notes supplémentaires'), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = _('Réservation')
        verbose_name_plural = _('Réservations')
        ordering = ['-date', '-time']
    
    def __str__(self):
        return f"{self.name} - {self.service} - {self.date} {self.time}"

class Service(models.Model):
    name = models.CharField(_('Nom'), max_length=100)
    description = models.TextField(_('Description'))
    price = models.DecimalField(_('Prix'), max_digits=10, decimal_places=2)
    duration = models.CharField(_('Durée'), max_length=50)
    image = CloudinaryField(_('Image'), folder='services/')
    order = models.IntegerField(_('Ordre d\'affichage'), default=0)
    is_active = models.BooleanField(_('Actif'), default=True)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')
        ordering = ['order']

    def __str__(self):
        return self.name

class Gallery(models.Model):
    CATEGORY_CHOICES = [
        ('coiffure', _('Coiffure')),
        ('maquillage', _('Maquillage')),
        ('soins', _('Soins')),
        ('manucure', _('Manucure')),
    ]

    title = models.CharField(_('Titre'), max_length=100)
    image = CloudinaryField(_('Image'), folder='gallery/')
    category = models.CharField(_('Catégorie'), max_length=20, choices=CATEGORY_CHOICES)
    order = models.IntegerField(_('Ordre d\'affichage'), default=0)
    is_active = models.BooleanField(_('Actif'), default=True)

    class Meta:
        verbose_name = _('Image Galerie')
        verbose_name_plural = _('Images Galerie')
        ordering = ['order']

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(_('Nom'), max_length=100)
    photo = CloudinaryField(_('Photo'), folder='testimonials/', blank=True)
    comment = models.TextField(_('Commentaire'))
    rating = models.IntegerField(_('Note'), choices=[(i, i) for i in range(1, 6)])
    is_active = models.BooleanField(_('Actif'), default=True)
    order = models.IntegerField(_('Ordre d\'affichage'), default=0)

    class Meta:
        verbose_name = _('Témoignage')
        verbose_name_plural = _('Témoignages')
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.rating}★"

class TeamMember(models.Model):
    name = models.CharField(_('Nom'), max_length=100)
    position = models.CharField(_('Poste'), max_length=100)
    photo = CloudinaryField(_('Photo'), folder='team/')
    description = models.TextField(_('Description'))
    order = models.IntegerField(_('Ordre d\'affichage'), default=0)
    is_active = models.BooleanField(_('Actif'), default=True)

    class Meta:
        verbose_name = _('Membre de l\'équipe')
        verbose_name_plural = _('Membres de l\'équipe')
        ordering = ['order']

    def __str__(self):
        return f"{self.name} - {self.position}"

class SiteSettings(models.Model):
    # General
    site_name = models.CharField(_('Nom du site'), max_length=100, default='Chez Ghizlane')
    logo = CloudinaryField(_('Logo'), folder='site/', null=True, blank=True)
    favicon = CloudinaryField(_('Favicon'), folder='site/', null=True, blank=True)
    
    # Hero Section
    hero_title = models.CharField(_('Titre Hero'), max_length=200)
    hero_subtitle = models.TextField(_('Sous-titre Hero'))
    hero_image = CloudinaryField(_('Image Hero'), folder='site/', null=True, blank=True)
    
    # Contact Info
    phone = models.CharField(_('Téléphone'), max_length=20)
    email = models.EmailField(_('Email'))
    address = models.TextField(_('Adresse'))
    google_maps_link = models.URLField(_('Lien Google Maps'))
    
    # Social Media
    facebook = models.URLField(_('Facebook'), blank=True)
    instagram = models.URLField(_('Instagram'), blank=True)
    tiktok = models.URLField(_('TikTok'), blank=True)
    
    # Business Hours
    business_hours = models.TextField(_('Horaires d\'ouverture'))
    
    # Footer
    footer_text = models.TextField(_('Texte du pied de page'))
    
    # About Section
    about_title = models.CharField(_('Titre À propos'), max_length=200)
    about_content = models.TextField(_('Contenu À propos'))
    about_image = CloudinaryField(_('Image À propos'), folder='site/', null=True, blank=True)

    class Meta:
        verbose_name = _('Paramètres du site')
        verbose_name_plural = _('Paramètres du site')

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        if SiteSettings.objects.exists() and not self.pk:
            raise ValidationError(_('Il ne peut y avoir qu\'une seule instance de SiteSettings'))
        return super().save(*args, **kwargs)

class Promotion(models.Model):
    title = models.CharField(_('Titre'), max_length=200)
    description = models.TextField(_('Description'))
    image = CloudinaryField(_('Image'), folder='promotions/')
    start_date = models.DateField(_('Date de début'))
    end_date = models.DateField(_('Date de fin'))
    is_active = models.BooleanField(_('Actif'), default=True)
    order = models.IntegerField(_('Ordre d\'affichage'), default=0)

    class Meta:
        verbose_name = _('Promotion')
        verbose_name_plural = _('Promotions')
        ordering = ['-start_date']

    def __str__(self):
        return self.title
