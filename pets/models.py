from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    owners = models.ManyToManyField(User)

    GENDER_CHOICES = [
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER'),
        ('N', 'NOT SPECIFIED'),
    ]
    
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='N',
        verbose_name='Gender'
    )

    def __str__(self):
        return f"{self.name} (id={self.id})"

