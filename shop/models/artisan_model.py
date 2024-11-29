from django.db import models

from accounts.models import UserModel


SEX = [
    ('M', 'Male'),
    ('F', 'Female'),   
]

JOB =[

    ('Coiffure', 'Coiffure'),
    ('Couture', 'Couture'),
    ('Mecanique', 'Mecanique'),
    ('Bijouterie', 'Bijouterie'),
    ('Maconnerie', 'Maconnerie'),
    ('Transport', 'Transport'),
    ('Electronique', 'Electronique'),
    ('Boucherie', 'Boucherie'),

]

class ArtisanModel(models.Model):
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='artisan_profile')

    job_artisan = models.CharField(max_length=255, choices=JOB)
    sex_artisan = models.CharField(max_length=1, choices=SEX)
    picture_artisan = models.URLField(max_length=500, null=True, blank=True)


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='artisan_groups',
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='artisan_permissions',
        blank=True
    )
    
    class Meta:
        verbose_name = "Artisan"
        verbose_name_plural = "Artisans"

    def __str__(self):
        return self.username
