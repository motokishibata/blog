from django.shortcuts import render
from myportfolio.models import Work, SkillSet, SkillCategory, Profile, UseSkill

def index(request):
    works = Work.objects.all()
    skill_sets = SkillSet.objects.order_by('sort_no').all()
    skill_categorys = SkillCategory.objects.order_by('sort_no').all()
    profile = Profile.objects.first()
    use_skill = UseSkill.objects.all()

    context = {'Works':works, 'SkillCategorys':skill_categorys,'SkillSets':skill_sets, 'Profile':profile, 'UseSkill':use_skill}

    return render(request, 'myportfolio/index.html', context)