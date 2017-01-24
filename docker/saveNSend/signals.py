from json import dumps

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from channels import Group

# from .models import Invitation


def send_notification(notification):
    print('send_notification. notification = {}'.format(notification))
    Group("notifications").send({'text': dumps(notification)})


# @receiver(post_save, sender=Invitation)
def invitation_post_save(sender, **kwargs):
    print("saved");
    send_notification({
        'name': 'Helen'
    })
