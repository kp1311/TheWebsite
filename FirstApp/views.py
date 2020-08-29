from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from FirstApp.forms import RegisterForm,ProfessionalResourcesForm,Personal_Development_ResourcesForm,Financial_Success_ResourcesForm,UserForm,MyGoalForm,MyLibraryForm,Challenge2Form,Challenge1Form,AddExperienceForm,CommentsandSuggestionsForm
from FirstApp.models import Professional_Resources,Personal_Development_Resources,Financial_Success_Resources,MyGoal,MyLibrary,Challenge1,Challenge2,AddExperience,CommentsandSuggestions
from datetime import date
import datetime
# Create your views here.
#Home Page View
from django.contrib.auth import authenticate,login,logout

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages


def detail12345(request):
    field1 = request.GET.get('field')
    resource=Professional_Resources.objects.filter(Field=field1).order_by('Title')

    return  render(request, "FirstApp/detail12345.html",{'Resource':resource,'field1':field1} )

# Create your views here.
def RegistrationView(response):
    form = RegisterForm()
    if response.method == "POST":
	       form = RegisterForm(response.POST)
	       if form.is_valid():
	              form.save()

	              return render(response, "FirstApp/Registration.html", {"forms":form,"message":"You have been registered"})
    return render(response, "FirstApp/Registration.html", {"forms":form})
def index(request):

    my_dict={'insert':"hello world"}
    return render(request,'FirstApp/Base.html',context=my_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


#This view is for Personal Development page
def Personal_Development(request):
    return render(request,'FirstApp/Personal_Development.html')

#This view is for Professional Development page
def Professional_Development(request):

    return render(request,'FirstApp/Professional_Development.html')

def DetailPersonalDevelopmentView(request):
    field1 = request.GET.get('author')
    print(field1)
    resource=Personal_Development_Resources.objects.filter(Author=field1).order_by('Name_Of_Resource')
    return render(request,'FirstApp/DetailPersonalDevelopment.html',{'Resource':resource})

#This view is for Financial Success page
def Financial_Success(request):

    return render(request,'FirstApp/Financial_Success.html')

#This view is for Add Resources page
def AddResourceView(request):
    form=ProfessionalResourcesForm()
    if request.method=="POST":
        form=ProfessionalResourcesForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request,'FirstApp/AddResource.html',{'forms':form,"message":"Thank you.Your response has been saved."})




    return render(request,'FirstApp/AddResource.html',{'forms':form})


def AddPersonalDevelopmentResourceView(request):
    form=Personal_Development_ResourcesForm()
    if request.method=="POST":
        form=Personal_Development_ResourcesForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return render(request,'FirstApp/Add_Personal_Development_Resource.html',{'forms':form,'message':"Thank You.Your data has been saved"})


    return render(request,'FirstApp/Add_Personal_Development_Resource.html',{'forms':form})


def FinancialSuccessView(request):
    ResourceList=Financial_Success_Resources.objects.all()
    return render(request,'FirstApp/Financial_Success.html',{'Resource':ResourceList})

def Add_Financial_Success_ResourceView(request):
    form=Financial_Success_ResourcesForm()
    if request.method=="POST":
        form=Financial_Succcess_ResourcesForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request,'FirstApp/Add_Financial_Success_Resource.html',{'forms':form,"message":"Thank You.You data has been saved."})

    return render(request,'FirstApp/Add_Financial_Success_Resource.html',{'forms':form})

def user_login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("account is not active")

        else:
             print("Someone else tried to login and failed")
             return HttpResponse("Invalid credentials")
    else:
         return render (request,'FirstApp/Login.html',{})


def MyGoalView(request):
    if request.user.is_authenticated:
       My_goal= MyGoal.objects.filter(user=request.user)

       if request.method=="POST":
          user1=request.user
          Subject1=request.POST.get('Subject')
          Url1=request.POST.get('Url')
          b1 = MyGoal(user=user1, Goal_subject=Subject1,Subject_Url=Url1)
          b1.save()
          return render(request,'FirstApp/MyGoal.html',{'goal':My_goal})



       else:
           return render(request,'FirstApp/MyGoal.html',{'goal':My_goal})

    else:
         return render(request,'FirstApp/Login.html',{"message":"You need to login to view this page"})




def MyLibraryView(request):
    if request.user.is_authenticated:
       My_Library= MyLibrary.objects.filter(user=request.user)


       if request.method=="POST":
          user1=request.user
          Subject1=request.POST.get('Subject')
          Author1=request.POST.get('Author')
          Url1=request.POST.get('Url')
          b1 = MyLibrary(user=user1, Subject=Subject1,Author=Author1,Url=Url1)
          b1.save()

          form=MyLibraryForm(request.POST)
          return render(request,'FirstApp/MyLibrary.html',{'MyLibrary':My_Library,"message":"Your data has been saved"})

       else:
            return render(request,'FirstApp/MyLibrary.html',{'MyLibrary':My_Library})



    else:
        return render(request,'FirstApp/Login.html',{'message':"You need to login to view this page."})


def Challenge2View(request):
    if request.user.is_authenticated:
       Challenge2Status= Challenge2.objects.filter(user=request.user)

       if request.method=="POST":
          user1=request.user
          Title1=request.POST.get('Title')
          Author1=request.POST.get('Author')
          Time1=date.today()
          b1 = Challenge2(user=user1,Book_Title=Title1,Book_Author=Author1,Time=Time1)
          b1.save()
          return render(request,'FirstApp/Challenge2.html',{'Challenge2Status':Challenge2Status,'message':"Your data has been saved"})

       else:
        return render(request,'FirstApp/Challenge2.html',{'Challenge2Status':Challenge2Status})

    else:
        return render(request,'FirstApp/Login.html',{'message':"You need to login to view this page."})


def Challenge1View(request):
    if request.user.is_authenticated:

       if request.method!='POST':
          return render(request,'FirstApp/Challenge1.html',{})

       else:
           Challenge1Status=Challenge1.objects.filter(user=request.user)
           if request.method=='POST':
              Challenge1Status2=Challenge1.objects.get(user=request.user)
              time=request.POST.get('Time')
              time2=int(time)
              if time2<=10:
                 Challenge1Status2.Hours_spent_learning+=time2
                 Challenge1Status2.save()
                 return render(request,'FirstApp/Challenge1.html',{'Challenge1Status':Challenge1Status,'message':"Your data has been saved"})
              else:
                  print("Time limit exceeded")

    else:
        return render(request,'FirstApp/Login.html',{'message':"You must be logged in to see this page."})


def ChallengeView(request):
    return render(request,'FirstApp/Challenge.html')


def AddExperienceView(request):
    form=AddExperienceForm()

    if request.method=='POST':
        form=AddExperienceForm(request.POST)

        if form.is_valid():
           form.save(commit=True)
           form=AddExperienceForm(request.POST)
           return render(request,'FirstApp/AddExperience.html',{'forms':form,'message':"Your information has been saved"})


    return render(request,'FirstApp/AddExperience.html',{'forms':form})


def AdvicePathsExperienceResourcesView(request):
    return render(request,'FirstApp/AdvicePathsExperienceResources.html')


def ThePageView(request):
    field_variable = request.GET['field_selected']
    Experience1=request.GET['Experience']
    AllDetails= AddExperience.objects.filter(field=field_variable).filter(Target_Section=Experience1)

    return render(request,'FirstApp/ThePage.html',{'AllDetails':AllDetails,'field1':field_variable})

def GetAJobView(request):
    return render(request,'FirstApp/GetAJob.html')


def GetAJobDetailView(request):
    field_variable=request.GET['field_selected']
    experience=request.GET['Experience']
    print (field_variable)
    field_variable=request.GET['field_selected']
    experience=request.GET['Experience']
    AllDetails= Professional_Resources.objects.filter(Field=field_variable).filter(Target_Audience=experience)
    return render(request,'FirstApp/GetAJobDetail.html',{'AllDetails':AllDetails,'Field':field_variable,'Experience':experience})

def NewPageView(request):
    return render(request,'FirstApp/NewPage.html')

def NewPageDetailsView(request):
    field_variable=request.GET['field_selected']
    today = datetime.date.today()
    previous_date = today - datetime.timedelta(days=15)
    print(previous_date)
    print(type(previous_date))
    AllDetails=Professional_Resources.objects.filter(Field=field_variable).filter(Released_On__gte=previous_date)
    return render(request,'FirstApp/NewPageDetails.html',{'AllDetails':AllDetails,'Field':field_variable})

def CommentsAndSuggestionsView(request):
    form=CommentsandSuggestionsForm()

    if request.method=='POST':
        form=CommentsandSuggestionsForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return render(request,'FirstApp/CommentsAndSuggestions.html',{'forms':form,'message':"Your suggestions and comments have been recorded."})

    return render(request,'FirstApp/CommentsAndSuggestions.html',{'forms':form})
