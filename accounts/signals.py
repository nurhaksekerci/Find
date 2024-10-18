from allauth.account.signals import user_signed_up
from django.dispatch import receiver

@receiver(user_signed_up)
def populate_profile(sociallogin, **kwargs):
    user = sociallogin.user

    # Google'dan gelen bilgiler
    if sociallogin.account.provider == 'google':
        extra_data = sociallogin.account.extra_data
        user.first_name = extra_data.get('given_name', '')
        user.last_name = extra_data.get('family_name', '')
        user.save()

