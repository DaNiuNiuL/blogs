from django.contrib import admin
from account.models import Profile,Contact
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','birth_date','photo')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('user_from','user_to','created')