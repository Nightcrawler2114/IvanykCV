from django.shortcuts import render, HttpResponseRedirect
from .forms import *
from .models import HobbiesAndInterest, PersonalFeature, Activity, Skill


# class MainView(TemplateView):
#     template_name = 'CV/base.html'
#     form = ContactMe
#     inter = HobbiesAndInterests.objects.all()
#     # form.save()


def main_view(request):
    form = ContactMe(request.POST or None)
    if form.is_valid():
            form.save()
            print('saved')
            return HttpResponseRedirect('CV/base.html')
    else:
        form = ContactMe()
        print('unsaved')

    hobbies_and_interests = HobbiesAndInterest.objects.all()
    personal_features = PersonalFeature.objects.all()
    skills = Skill.objects.all()
    activity = Activity.objects.all()
    skills_blue = Skill.objects.get(skill='Versatility')
    return render(request, 'CV/base.html', locals())
