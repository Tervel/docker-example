from django.db import models
from django.contrib.auth.models import User

from channels import Channel

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .signals import invitation_post_save

# Temp
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver

# from channels import Group


class Invitation(models.Model):

    email = models.EmailField()
    sent = models.DateTimeField(null=True)
    sender = models.ForeignKey(User)
    key = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return "{} invited {}".format(self.sender, self.email)

    class Meta:
        verbose_name_plural = "Invitations"

# Temp

post_save.connect(invitation_post_save, sender=Invitation)

# def send_notification(notification):
#     print('send_notification. notification = {}'.format(notification))
#     Group("notifications").send({'text': 'Hello world!'})


# @receiver(post_save, sender=Invitation)
# def invitation_post_save(sender, **kwargs):
#     print("saved");
#     send_notification({
#         'text': 'Saved!'
#     })

