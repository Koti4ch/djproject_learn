from django.contrib import admin
from account.models import UserProfile
# Register your models here.




@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'photo')

