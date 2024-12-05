# Generated by Django 5.1.3 on 2024-12-05 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='Image')),
                ('category', models.CharField(choices=[('coiffure', 'Coiffure'), ('maquillage', 'Maquillage'), ('soins', 'Soins'), ('manucure', 'Manucure')], max_length=20, verbose_name='Catégorie')),
                ('order', models.IntegerField(default=0, verbose_name="Ordre d'affichage")),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
            ],
            options={
                'verbose_name': 'Image Galerie',
                'verbose_name_plural': 'Images Galerie',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titre')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='promotions/', verbose_name='Image')),
                ('start_date', models.DateField(verbose_name='Date de début')),
                ('end_date', models.DateField(verbose_name='Date de fin')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('order', models.IntegerField(default=0, verbose_name="Ordre d'affichage")),
            ],
            options={
                'verbose_name': 'Promotion',
                'verbose_name_plural': 'Promotions',
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Prix')),
                ('duration', models.CharField(max_length=50, verbose_name='Durée')),
                ('image', models.ImageField(upload_to='services/', verbose_name='Image')),
                ('order', models.IntegerField(default=0, verbose_name="Ordre d'affichage")),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(default='Chez Ghizlane', max_length=100, verbose_name='Nom du site')),
                ('logo', models.ImageField(upload_to='site/', verbose_name='Logo')),
                ('favicon', models.ImageField(upload_to='site/', verbose_name='Favicon')),
                ('hero_title', models.CharField(max_length=200, verbose_name='Titre Hero')),
                ('hero_subtitle', models.TextField(verbose_name='Sous-titre Hero')),
                ('hero_image', models.ImageField(upload_to='site/', verbose_name='Image Hero')),
                ('phone', models.CharField(max_length=20, verbose_name='Téléphone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('address', models.TextField(verbose_name='Adresse')),
                ('google_maps_link', models.URLField(verbose_name='Lien Google Maps')),
                ('facebook', models.URLField(blank=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, verbose_name='Instagram')),
                ('tiktok', models.URLField(blank=True, verbose_name='TikTok')),
                ('business_hours', models.TextField(verbose_name="Horaires d'ouverture")),
                ('footer_text', models.TextField(verbose_name='Texte du pied de page')),
                ('about_title', models.CharField(max_length=200, verbose_name='Titre À propos')),
                ('about_content', models.TextField(verbose_name='Contenu À propos')),
                ('about_image', models.ImageField(upload_to='site/', verbose_name='Image À propos')),
            ],
            options={
                'verbose_name': 'Paramètres du site',
                'verbose_name_plural': 'Paramètres du site',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('position', models.CharField(max_length=100, verbose_name='Poste')),
                ('photo', models.ImageField(upload_to='team/', verbose_name='Photo')),
                ('description', models.TextField(verbose_name='Description')),
                ('order', models.IntegerField(default=0, verbose_name="Ordre d'affichage")),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
            ],
            options={
                'verbose_name': "Membre de l'équipe",
                'verbose_name_plural': "Membres de l'équipe",
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('photo', models.ImageField(blank=True, upload_to='testimonials/', verbose_name='Photo')),
                ('comment', models.TextField(verbose_name='Commentaire')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], verbose_name='Note')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('order', models.IntegerField(default=0, verbose_name="Ordre d'affichage")),
            ],
            options={
                'verbose_name': 'Témoignage',
                'verbose_name_plural': 'Témoignages',
                'ordering': ['order'],
            },
        ),
    ]
