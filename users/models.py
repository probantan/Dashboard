# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    image = models.ImageField( default ='defaul.jpg',upload_to='prof', blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True, null =True)

    def __str__(self):
        return self.user.username
    
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()



from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now

# Create your models h

LITRES = (
    ('40Ltrs', '40Ltrs'),
    ('60Ltrs', '60Ltrs'),
    ('80Ltrs', '80Ltrs'),
    ('100Ltrs', '100Ltrs'),
    ('120Ltrs', '120Ltrs'),
    ('140Ltrs', '140Ltrs'),
    ('160Ltrs', '160Ltrs'),
    ('180Ltrs', '180Ltrs'),
    ('200Ltrs', '200Ltrs'),
    ('300Ltrs', '300Ltrs'),
    ('1000Ltrs', '1000Ltrs'),
    ('2000Ltrs', '2000Ltrs'),
    ('3000Ltrs', '3000Ltrs'),
    ('4000Ltrs', '4000Ltrs'),
    ('5000Ltrs', '5000Ltrs'),
    ('10000Ltrs', '1000Ltrs'),

)
class customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)

    location= models.CharField(max_length=120)
    Litres= models.CharField(max_length=120, choices=LITRES, default='40Ltrs')
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
            return self.name