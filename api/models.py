from django.db import models
from accounts.models import CustomUserModel
# Create your models here.

class UserIp(models.Model):
    user = models.OneToOneField(CustomUserModel, verbose_name=("User"), on_delete=models.SET_DEFAULT, default="Silindi")
    register_ip = models.CharField(verbose_name=("Register IP"), max_length=50, blank=True, null= True)
    mail_verified = models.BooleanField(verbose_name=("Verified?"), default=False)
    mail_verified_at = models.DateField(verbose_name=("Mail Verified At"), blank=True, null= True)
    change_pass_at = models.DateField(verbose_name=("Password Verified At"), blank=True, null= True)
    is_delete = models.BooleanField(verbose_name=("Delete?"), default=False)
    country = models.CharField(verbose_name=("Country"), max_length=100, blank=True, null= True)
    city = models.CharField(verbose_name=("City"), max_length=256, blank=True, null= True)
    language = models.CharField(verbose_name=("Language"), max_length=50, blank=True, null= True)
    last_send_mail = models.DateField(verbose_name=("Send Mail At"), blank=True, null= True)


    def __str__(self):
        return f"{self.user} - {self.register_ip}"
    

class APIInfo(models.Model):
    name = models.CharField(verbose_name=("Api Name"), max_length=256)
    api_key = models.CharField(verbose_name=("Api Key"), max_length=256)
    detail = models.TextField(verbose_name=("Api Detail"))
    client_id = models.CharField(verbose_name=("Client Id"), max_length=255, blank=True, null=True)
    client_secret = models.CharField(verbose_name=("Client Secret"), max_length=255, blank=True, null=True)
    doc_url = models.CharField(verbose_name=("Api Doc Url"), max_length=256)
    spare_1 = models.CharField(verbose_name=("Spare 1"), max_length=255, blank=True, null=True)
    spare_2 = models.CharField(verbose_name=("Spare 2"), max_length=255, blank=True, null=True)
    spare_3 = models.CharField(verbose_name=("Spare 3"), max_length=255, blank=True, null=True)
    spare_4 = models.CharField(verbose_name=("Spare 4"), max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.doc_url}"
    

class SponsorInfo(models.Model):
    widget_number = models.PositiveIntegerField(verbose_name=("Widget Number"))
    name = models.CharField(verbose_name=("Sponsor Name"), max_length=256)
    number = models.CharField(verbose_name=("Sponsor Lct"), max_length=2)
    is_active = models.BooleanField(verbose_name=("Active?"), default=True)
    code = models.TextField(verbose_name=("Iframe Code"))

    def __str__(self):
        return f"{self.name} - {self.number}"


class New(models.Model):
    NEW_CATEGORY = [
        ('General', 'General'),
        ('Business', 'Business'),
        ('Entertainment', 'Entertainment'),
        ('Health', 'Health'),
        ('Technology', 'Technology'),
    ]
    widget_number = models.PositiveIntegerField(verbose_name=("Widget Number"))
    user = models.OneToOneField(CustomUserModel, verbose_name=("User"), on_delete=models.CASCADE)
    country = models.CharField(verbose_name=("Country"), max_length=100)
    language = models.CharField(verbose_name=("Language"), max_length=50)
    category = models.CharField(verbose_name=("Category"), choices=NEW_CATEGORY, max_length=256)

    def __str__(self):
        return f"{self.category} - {self.language}"

class Todo(models.Model):
    widget_number = models.PositiveIntegerField(verbose_name=("Widget Number"))
    user = models.OneToOneField(CustomUserModel, verbose_name=("User"), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=("Todo Name"), max_length=256)
    is_complete = models.BooleanField(verbose_name=("Complete?"))
    created_at = models.DateTimeField(verbose_name=("Created At"), auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.is_complete}"

class Shortcut(models.Model):
    widget_number = models.PositiveIntegerField(verbose_name=("Widget Number"))
    user = models.OneToOneField(CustomUserModel, verbose_name=("User"), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=("Shortcut Name"), max_length=256)
    url = models.CharField(verbose_name=("Shortcut Url"), max_length=256)
    created_at = models.DateTimeField(verbose_name=("Created At"), auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.url}"


class Alarm(models.Model):
    ADDITIONAL_INFO = [
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    ]
    widget_number = models.PositiveIntegerField(verbose_name=("Widget Number"))
    user = models.OneToOneField(CustomUserModel, verbose_name=("User"), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=("Alarm Name"), max_length=256)
    additional_info = models.CharField(verbose_name=("Additional Info"), choices=ADDITIONAL_INFO, max_length=50)
    is_active = models.BooleanField(verbose_name=("Active?"), default=True)

    def __str__(self):
        return f"{self.name} - {self.additional_info}"


class FinanceCategory(models.Model):
    category = models.CharField(verbose_name=("Finans Category"), max_length=256)

    def __str__(self): 
        self.category

class Finance(models.Model):

    widget_number = models.PositiveIntegerField(verbose_name=("Widget Number"))
    user = models.OneToOneField(CustomUserModel, verbose_name=("User"), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=("Alarm Name"), max_length=256)
    categories = models.ManyToManyField(FinanceCategory, verbose_name=("Finance Category"))

    def __str__(self): 
        self.name

class Note(models.Model):
    widget_number = models.PositiveIntegerField(verbose_name=("Widget Number"))
    user = models.OneToOneField(CustomUserModel, verbose_name=("User"), on_delete=models.CASCADE)
    note = models.CharField(verbose_name=("Note"), max_length=500)

    def __str__(self): 
        self.note

class GetUp(models.Model):
    widget_number = models.PositiveIntegerField(verbose_name=("Widget Number"))
    user = models.OneToOneField(CustomUserModel, verbose_name=("User"), on_delete=models.CASCADE)
    exercise = models.PositiveIntegerField(verbose_name=("Exercise Point"))
    reminder = models.PositiveIntegerField(verbose_name=("Reminder Point"))
    date = models.DateField(verbose_name=("Date"))

    def __str__(self):
        return f"{self.date} - {self.exercise} - {self.reminder}"

class Image(models.Model):
    widget_number = models.PositiveIntegerField(verbose_name=("Widget Number"))
    user = models.OneToOneField(CustomUserModel, verbose_name=("User"), on_delete=models.CASCADE)
    image = models.FileField(verbose_name=("İmage"), upload_to="images/", max_length=255)

    def __str__(self): 
        self.image

class Quotes(models.Model):
    widget_number = models.PositiveIntegerField(verbose_name=("Widget Number"))
    user = models.OneToOneField(CustomUserModel, verbose_name=("User"), on_delete=models.CASCADE)
    text = models.CharField(verbose_name=("Quotes Text"), max_length=256)

    def __str__(self): 
        self.text