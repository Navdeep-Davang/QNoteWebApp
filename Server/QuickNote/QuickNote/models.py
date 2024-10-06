from django.db import models
from django.utils import timezone

# Created QNoteWeb application details module from home page of web side
class QNoteWeb(models.Model):

    qNote_id = models.AutoField(primary_key=True) # qNote web details primary key field
    description = models.TextField(null=False, blank=False) # qNote web detail description field
    qNote_logo = models.ImageField(null=False, blank=False) # qNote web logo image field
    contact_address = models.TextField(null=False, blank=False) # qNote web contact address detail field
    contact_email = models.CharField(max_length=50, null=False, blank=False) # qNote web contact email detail field
    contact_number = models.CharField(max_length=10, null=False, blank=False) # qNote web contact number detail field
    terms_condition = models.TextField(null=False, blank=False) # qNote web terms and conditions detail field
    created_at = models.DateTimeField(default=not timezone.now()) # qNote web created date and time detail field
    updated_at = models.DateTimeField(auto_now=True) # qNote web updated date and time detail field

    def __str__(self):
        return self.description