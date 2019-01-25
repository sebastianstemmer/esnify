from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_countries.fields import CountryField

# Zuerst: Daten-Modellierung:
# - Semantisches (konzeptionelles) Schema: Entity-Relationsship-Modell (ERM)
# - Logisches (relationales) Schema
#
# Anschließend Konzeptuelles (physisches) Schema mittels Django ORM:


class StayAbroad(models.Model):

    month_amount = models.PositiveIntegerField()
    country = CountryField()

    def __str__(self):
        return "{} month in {}".format(self.month_amount, self.country)


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    beispiel = models.CharField(max_length=32)
    #stay_abroad = models.ForeignKey(StayAbroad, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.user.username

    def meta(self):
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('profile_page', args=[str(self.pk)])

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    #
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()
