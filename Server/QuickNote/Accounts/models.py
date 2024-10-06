from django.db import models
from django.utils import timezone

# Created User Account module to store user related information
class UserAccount(models.Model):

    # Fields based on the table your shared
    user_id = models.AutoField(primary_key=True) # Equivalent to SERIAL in SQL
    username = models.CharField(max_length=50, unique=True, null=False) # VARCHAR(50), UNIQUE, NOT NULL
    email = models.EmailField(max_length=100, unique=True, null=False) # VARCHAR(100), UNIQUE, NOT NULL
    password_hash = models.TextField(null=False) # TEXT, NOT NULL
    confirm_password_hash = models.TextField(null=False) # TEXT, NOT NULL
    profile_picture = models.ImageField(upload_to='profile_picture/', null=True, blank=True) # Image field, ALLOW NULL
    created_at = models.DateTimeField(default=timezone.now) # TIMESTAMP, DEFAULT CURRENT_TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) # Automatically set last modified timestamp

    def __str__(self):
        return self.username  # String representation of the object
