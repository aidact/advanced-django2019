from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from auth_.models import MainUser, Profile
from auth_.serializers import ProfileSerializer


@receiver(post_save, sender=MainUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(pre_delete, sender=MainUser)
def profile_delete(sender, instance, **kwargs):
    try:
        print(instance.profile)
        with open("profiles.json", "w") as out:
            # profile = Profile.objects.get(user_id=instance.id)
            data = ProfileSerializer(instance.profile)
            out.write(data)
    except Exception as e:
        print(e)

