from django.db import models
from django.contrib.auth.models import User

FieldChoices = (
    ('College Students','College Students'),
    ('0-2 yrs experience', '0-2 yrs experience'),
    ('2-5 yrs experience','2-5 yrs experience'),
    ('5-10 yrs experience','5-10 yrs experience'),
    ('10-15 yrs experience','10-15 yrs experience'),
    ('15-20 yrs experience','15-20 yrs experience'),
)

# Create your models here.
class Professional_Resources(models.Model):
    Title=models.CharField(max_length=100)
    Field=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)
    Description=models.TextField()
    Url=models.URLField(max_length=264)
    Target_Audience =models.CharField(max_length=20, choices=FieldChoices)
    Type=models.CharField(max_length=20)
    Self_Email=models.EmailField(max_length=100)
    Price=models.IntegerField()
    Released_On=models.DateField()

    def __str__(self):
        return self.Title


class Personal_Development_Resources(models.Model):
    Author=models.CharField(max_length=25)
    Name_Of_Resource=models.CharField(max_length=100)
    Url=models.URLField(max_length=150)
    Type=models.CharField(max_length=25)
    Self_Email=models.EmailField(max_length=100)
    Price=models.IntegerField()
    Released_On=models.DateField()

    def __str__(self):
        return self.Name_Of_Resource


class Financial_Success_Resources(models.Model):
    Author=models.CharField(max_length=25)
    Name_Of_Resource=models.CharField(max_length=100)
    Url=models.URLField(max_length=150)
    Type=models.CharField(max_length=25)
    Self_Email=models.EmailField(max_length=100)
    Price=models.IntegerField()
    Released_On=models.DateField()

    def __str__(self):
        return self.Name_Of_Resource

class MyGoal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Goal_subject=models.CharField(max_length=50)
    Subject_Url=models.URLField()

    def __str__(self):
        return self.Goal_Url

class MyLibrary(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Subject=models.CharField(max_length=50)
    Author=models.CharField(max_length=50)
    Url=models.URLField()

    def __str__(self):
        return self.Goal_Url


class Challenge1(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Start_Date=models.DateField()
    Hours_spent_learning=models.IntegerField()

    def __str__(self):
        return str(self.user)


class Challenge2(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Time=models.DateField()
    Book_Title=models.CharField(max_length=75)
    Book_Author=models.CharField(max_length=50)


    def __str__(self):
        return self.Book_Title

class AddExperience(models.Model):
     User_Name=models.CharField(max_length=50)
     Role=models.CharField(max_length=50)
     Company=models.CharField(max_length=50)
     field=models.CharField(max_length=50)
     Target_Section=models.CharField(max_length=25)
     AdviceforGoalAttainment=models.TextField()
     SelfExperience=models.TextField()
     Paths=models.TextField()
     ResourcesUsed=models.TextField()

     def __str__(self):
         return self.AdviceforGoalAttainment


class CommentsandSuggestions(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Comments=models.TextField()
    Suggestions=models.TextField()


    def __str__(self):
        return self.Comments
