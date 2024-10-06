from django.db import models
from Accounts.models import UserAccount

# created folder module to store folder details
class Folder(models.Model):
    folder_id = models.AutoField(primary_key=True)  # SERIAL equivalent
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)  # ForeignKey referencing UserAccount
    folder_name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)  # Optional description
    category = models.CharField(max_length=50, null=False)  # Category filter
    created_at = models.DateTimeField(auto_now_add=True)  # Default CURRENT_TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True)  # Updated at the last modification time

    def __str__(self):
        return self.folder_name

# created Note module to store notes in the folder
class Note(models.Model):
    note_id = models.AutoField(primary_key=True)  # SERIAL equivalent
    folder_id = models.ForeignKey(Folder, on_delete=models.CASCADE)  # ForeignKey referencing Folder
    user_id = models.ForeignKey(UserAccount, on_delete=models.CASCADE)  # ForeignKey referencing UserAccount
    note_title = models.CharField(max_length=200, null=False)  # VARCHAR(200), NOT NULL
    note_content = models.TextField(null=False)  # TEXT, NOT NULL
    created_at = models.DateTimeField(auto_now_add=True)  # DEFAULT CURRENT_TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True)  # DEFAULT CURRENT_TIMESTAMP on update

    def __str__(self):
        return self.note_title
