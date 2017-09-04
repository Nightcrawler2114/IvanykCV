from django.db import models


class ContactFace(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
    message = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return self.name


class PersonalFeature(models.Model):
    feature = models.TextField()

    def __str__(self):
        return self.feature


class HobbiesAndInterest(models.Model):
    interest = models.TextField()

    def __str__(self):
        return self.interest


class Activity(models.Model):
    activity = models.TextField(max_length=120)

    def __str__(self):
        return self.activity


class Skill(models.Model):
    skill = models.TextField(max_length=120)

    def __str__(self):
        return self.skill