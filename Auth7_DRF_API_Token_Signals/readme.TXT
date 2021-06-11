#Token generate using Signals

#settings.py file changes
INSTALLED_APPS = [
    .................
    'rest_framework',
    'rest_framework.authtoken',
    'api',
]

#model.py file code
#Token Generate namespace
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
#Token Generate Code here
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

