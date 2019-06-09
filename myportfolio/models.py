from django.db import models

class Work(models.Model):

    name = models.CharField(max_length=50)
    url_description = models.CharField(max_length=20, null=True)
    url = models.URLField(max_length=200, null=True)
    image = models.ImageField(upload_to='work-image')
    description = models.TextField()
    creation_start_date = models.DateField()
    creation_complete_date = models.DateField(null=True)

    def __str__(self):
        return self.name

class SkillCategory(models.Model):
    
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class SkillSet(models.Model):

    skill_category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    skill = models.CharField(max_length=50)
    experience = models.CharField(max_length=200)

    CATEGORY_FRONT_END = 1
    CATEGORY_BACK_END = 2
    CATEGORY_DB = 3
    CATEGORY_SERVER = 4
    CATEGORY_OS = 5
    CATEGORY_AUTHOR = 6

    def __str__(self):
        return self.skill

class Profile(models.Model):

    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    birth = models.DateField()
    address = models.CharField(max_length=100)
    career = models.TextField()
    introduction = models.TextField()
    image = models.ImageField(upload_to="profile", null=True)

    @property
    def full_name(self):
        return '{0} {1}'.format(self.first_name, self.last_name)

    def __str__(self):
        return self.full_name

class UseSkill(models.Model):

    work = models.ForeignKey(Work, on_delete=models.CASCADE)
    use_skill = models.ForeignKey(SkillSet, on_delete=models.CASCADE)

    def __str__(self):
        return self.use_skill.skill