from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=20, verbose_name='Імя', blank=True)
    last_name = models.CharField(max_length=20, verbose_name='Прізвище', blank=True)
    city = models.CharField(max_length=20, verbose_name='Назва населеного пункту', blank=True)
    address = models.CharField(max_length=100, verbose_name='номер відділення нової пошти ', blank=True)
    phone_number = models.BigIntegerField(verbose_name='Номер телефону', blank=True, null=True)
    objects = models.Manager()

    class Meta:
        ordering = ('user',)
        verbose_name = 'Профіль'
        verbose_name_plural = 'Профілі'

    def __str__(self):
        return self.first_name

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance, status='Новий покупець', email=instance.phone)
    post_save.connect(create_user_profile, sender=User)

