from django.shortcuts import render
from myportfolio.models import Work, SkillSet, SkillCategory, Profile

def index(request):
    works = Work.objects.all()
    skill_sets = SkillSet.objects.all()
    skill_categorys = SkillCategory.objects.all()
    profile = Profile.objects.first()

    context = {'Works':works, 'SkillCategorys':skill_categorys,'SkillSets':skill_sets, 'Profile':profile}

    return render(request, 'myportfolio/index.html', context)