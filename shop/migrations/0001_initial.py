# Generated by Django 5.1.2 on 2024-11-12 16:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtisanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_artisan', models.CharField(choices=[('Coiffure', 'Coiffure'), ('Couture', 'Couture'), ('Mecanique', 'Mecanique'), ('Bijouterie', 'Bijouterie'), ('Maconnerie', 'Maconnerie'), ('Transport', 'Transport'), ('Electronique', 'Electronique'), ('Boucherie', 'Boucherie')], max_length=255)),
                ('sex_artisan', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('picture_artisan', models.URLField(blank=True, max_length=500, null=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='artisan_groups', to='auth.group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='artisan_profile', to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='artisan_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'Artisan',
                'verbose_name_plural': 'Artisans',
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.TextField(max_length=500)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_picture', models.URLField(blank=True, null=True)),
                ('artisan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.artisanmodel')),
                ('groups', models.ManyToManyField(blank=True, related_name='product_users', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='product_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]