from django.contrib import admin
from .models import *


class ContactFaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']

    class Meta:
        model = ContactFace

admin.site.register({ContactFace, HobbiesAndInterest, PersonalFeature, Skill, Activity})

