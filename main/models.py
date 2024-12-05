from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

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
