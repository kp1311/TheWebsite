
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from FirstApp.forms import RegisterForm,ProfessionalResourcesForm,Personal_Development_ResourcesForm,Financial_Success_ResourcesForm,UserForm,MyGoalForm,MyLibraryForm,Challenge2Form,Challenge1Form,AddExperienceForm,GetAJobForm,CommentsandSuggestionsForm
from FirstApp.models import Professional_Resources,Personal_Development_Resources,Financial_Success_Resources,MyGoal,MyLibrary,Challenge1,Challenge2,AddExperience,GetAJob,CommentsandSuggestions
from datetime import date
import datetime
# Create your views here.
#Home Page View
from django.contrib.auth import authenticate,login,logout

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages


# Create your views here.
def RegistrationView(response):
    if response.method == "POST":
	       form = RegisterForm(response.POST)
	       if form.is_valid():
	              form.save()

	              return render(response, "FirstApp/Registration.html", {"forms":form,"message":"You have been registered"})
    else:
	     form = RegisterForm()

    return render(response, "FirstApp/Registration.html", {"forms":form})

def index(request):

    my_dict={'insert':"hello world"}
    return render(request,'FirstApp/Base.html',context=my_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
#This view is for Software Development page
def SoftwareDevelopmentView(request):
    ResourceList=Professional_Resources.objects.filter(Field="Software development").order_by('Title')


    return render(request,'FirstApp/Software_Development.html',{'Resource':ResourceList})

#This view is for Backup page
def BackupView(request):
    ResourceList=Professional_Resources.objects.filter(Field="Backup")


    return render(request,'FirstApp/Backup.html',{'Resource':ResourceList})

#This view is for Bank_View page
def Bank_PoView(request):
    ResourceList=Professional_Resources.objects.filter(Field="Bank Po")


    return render(request,'FirstApp/Bank_Po.html',{'Resource':ResourceList})

#This view is for Business page
def BusinessView(request):
    ResourceList=Professional_Resources.objects.filter(Field="Business")


    return render(request,'FirstApp/Business.html',{'Resource':ResourceList})

#This view is for CAT page
def CATView(request):
    ResourceList=Professional_Resources.objects.filter(Field="CAT")


    return render(request,'FirstApp/CAT.html',{'Resource':ResourceList})

#This view is for Database page
def DatabaseView(request):
    ResourceList=Professional_Resources.objects.filter(Field="Database")


    return render(request,'FirstApp/Database.html',{'Resource':ResourceList})

#This view is for GMAT page
def GMATView(request):
    ResourceList=Professional_Resources.objects.filter(Field="GMAT")


    return render(request,'FirstApp/GMAT.html',{'Resource':ResourceList})

#This view is for IAS page
def IASView(request):
    ResourceList=Professional_Resources.objects.filter(Field="IAS")
    return render(request,'FirstApp/IAS.html',{'Resource':ResourceList})


#This view is for Linux page
def LinuxView(request):
    ResourceList=Professional_Resources.objects.filter(Field="Linux")


    return render(request,'FirstApp/Linux.html',{'Resource':ResourceList})

#This view is for Medical page
def MedicalView(request):
    ResourceList=Professional_Resources.objects.filter(Field="Medical")


    return render(request,'FirstApp/Medical.html',{'Resource':ResourceList})

#This view is for Networking page
def NetworkingView(request):
    ResourceList=Professional_Resources.objects.filter(Field="Networking")


    return render(request,'FirstApp/Networking.html',{'Resource':ResourceList})

#This view is for SSC_CGL page
def SSC_CGLView(request):
    ResourceList=Professional_Resources.objects.filter(Field="SSC CGL")


    return render(request,'FirstApp/SSC_CGL.html',{'Resource':ResourceList})

#This view is for Storage page
def StorageView(request):
    ResourceList=Professional_Resources.objects.filter(Field="Storage")


    return render(request,'FirstApp/Storage.html',{'Resource':ResourceList})

#This view is for Swimming page
def SwimmingView(request):
    ResourceList=Professional_Resources.objects.filter(Field="Swimming")


    return render(request,'FirstApp/Swimming.html',{'Resource':ResourceList})

#This view is for Wintel page
def WintelView(request):
    ResourceList=Professional_Resources.objects.filter(Field="Wintel")


    return render(request,'FirstApp/Wintel.html',{'Resource':ResourceList})

#This view is for Personal Development page
def Personal_Development(request):
    return render(request,'FirstApp/Personal_Development.html')

#This view is for Professional Development page
def Professional_Development(request):
    return render(request,'FirstApp/Professional_Development.html')

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
            return index(request)

        else:
            print("Invalid form")

    return render(request,'FirstApp/AddResource.html',{'forms':form,"message":"Thsnk you.Your response has been saved."})

def BrianTracyView(request):
    ResourceList=Personal_Development_Resources.objects.filter(Author="Brian Tracy")


    return render(request,'FirstApp/Brian_Tracy.html',{'Resource':ResourceList})

def DeepakChopraView(request):
    ResourceList=Personal_Development_Resources.objects.filter(Author="Deepak Chopra")


    return render(request,'FirstApp/Deepak_Chopra.html',{'Resource':ResourceList})

def EarlNightingaleView(request):
    ResourceList=Personal_Development_Resources.objects.filter(Author="Earl Nightingale")


    return render(request,'FirstApp/Earl_Nightingale.html',{'Resource':ResourceList})

def JackCanfieldView(request):
    ResourceList=Personal_Development_Resources.objects.filter(Author="Jack Canfield")


    return render(request,'FirstApp/Jack_Canfield.html',{'Resource':ResourceList})

def JimRohnView(request):
    ResourceList=Personal_Development_Resources.objects.filter(Author="Jim Rohn")


    return render(request,'FirstApp/Jim_Rohn.html',{'Resource':ResourceList})

def NapoleanHillView(request):
    ResourceList=Personal_Development_Resources.objects.filter(Author="Napolean Hill")


    return render(request,'FirstApp/Napolean_Hill.html',{'Resource':ResourceList})

def RobinSharmaView(request):
    ResourceList=Personal_Development_Resources.objects.filter(Author="Robin Sharma")


    return render(request,'FirstApp/Robin_Sharma.html',{'Resource':ResourceList})

def ShivKheraView(request):
    ResourceList=Personal_Development_Resources.objects.filter(Author="Shiv Khera")


    return render(request,'FirstApp/Shiv_Khera.html',{'Resource':ResourceList})

def StevenRCoveyView(request):
    ResourceList=Personal_Development_Resources.objects.filter(Author="Steven R Covey")


    return render(request,'FirstApp/Steven_R_Covey.html',{'Resource':ResourceList})

def TonyRobbinsView(request):
    ResourceList=Personal_Development_Resources.objects.filter(Author="Tony Robbins")


    return render(request,'FirstApp/Tony_Robbins.html',{'Resource':ResourceList})

def WayneDyerView(request):
    ResourceList=Personal_Development_Resources.objects.filter(Author="Wayne Dyer")


    return render(request,'FirstApp/Wayne_Dyer.html',{'Resource':ResourceList})

def ZigZiglarView(request):
    ResourceList=Personal_Development_Resources.objects.filter(Author="Zig Ziglar")


    return render(request,'FirstApp/Zig_Ziglar.html',{'Resource':ResourceList})


def AddPersonalDevelopmentResourceView(request):
    form=Personal_Development_ResourcesForm()
    if request.method=="POST":
        form=Personal_Development_ResourcesForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return render(request,'FirstApp/Add_Personal_Development_Resource.html',{'forms':form,'message':"Thank You.Your data has been saved"})


        else:
            print("Invalid form")

    return render(request,'FirstApp/Add_Personal_Development_Resource.html',{'forms':form})


def BrianTracyFinancialSuccessView(request):
    ResourceList=Financial_Success_Resources.objects.filter(Author="Brian Tracy")
    return render(request,'FirstApp/BrianTracyFinancialSuccess.html',{'Resource':ResourceList})


def RobertKiyosakiFinancialSuccessView(request):
    ResourceList=Financial_Success_Resources.objects.filter(Author="Robert Kiyosaki")
    return render(request,'FirstApp/RobertKiyosakiFinancialSuccess.html',{'Resource':ResourceList})

def TonyRobbinsFinancialSuccessView(request):
    ResourceList=Financial_Success_Resources.objects.filter(Author="Tony Robbins")
    return render(request,'FirstApp/TonyRobbinsFinancialSuccess.html',{'Resource':ResourceList})

def OtherFinancialSuccessView(request):
    ResourceList=Financial_Success_Resources.objects.filter(Author="Other")
    return render(request,'FirstApp/OtherFinancialSuccess.html',{'Resource':ResourceList})

def Add_Financial_Success_ResourceView(request):
    form=Financial_Success_ResourcesForm()
    if request.method=="POST":
        form=Financial_Succcess_ResourcesForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request,'FirstApp/Add_Financial_Success_Resource.html',{'forms':form,"message":"Thank You.You data has been saved."})

        else:
            print("Invalid form")

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

@login_required
def MyGoalView(request):
    My_goal= MyGoal.objects.filter(user=request.user)

    form=MyGoalForm()


    if request.method=="POST":
        form=MyGoalForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

        else:
            print("Invalid form")

    return render(request,'FirstApp/MyGoal.html',{'forms':form,'goal':My_goal,"message":"Your data has been saved"})

@login_required
def MyLibraryView(request):
    My_Library= MyLibrary.objects.filter(user=request.user)

    form=MyLibraryForm()
    if request.method=="POST":
        form=MyLibraryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request,'FirstApp/MyLibrary.html',{'forms':form,'MyLibrary':My_Library,"message":"Your data has been saved"})

        else:
            print("Invalid form")

    return render(request,'FirstApp/MyLibrary.html',{'forms':form,'MyLibrary':My_Library})


def Challenge2View(request):
    Challenge2Status= Challenge2.objects.filter(user=request.user)

    form=Challenge2Form()
    if request.method=="POST":
        form=Challenge2Form(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request,'FirstApp/Challenge2.html',{'forms':form,'Challenge2Status':Challenge2Status,'message':"Your data has been saved"})

        else:
            print("Invalid form")

    return render(request,'FirstApp/Challenge2.html',{'forms':form,'Challenge2Status':Challenge2Status})


def Challenge1View(request):
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



    return render(request,'FirstApp/Challenge1.html',{'Challenge1Status':Challenge1Status})


def ChallengeView(request):
    return render(request,'FirstApp/Challenge.html')


def AddExperienceView(request):
    form=AddExperienceForm()

    if request.method=='POST':
        form=AddExperience(request.POST)

        if form.is_valid():
            form.save()
            return render(request,'FirstApp/AddExperience.html',{'forms':form,'message':"Your information has been saved"})


    return render(request,'FirstApp/AddExperience.html',{'forms':form})


def AdvicePathsExperienceResourcesView(request):
    return render(request,'FirstApp/AdvicePathsExperienceResources.html')


def ThePageView(request):
    field_variable = request.GET['field']
    AllDetails= AddExperience.objects.filter(field=field_variable)

    return render(request,'FirstApp/ThePage.html',{'AllDetails':AllDetails})

def GetAJobView(request):
    return render(request,'FirstApp/GetAJob.html')


def GetAJobDetailView(request):
    field_variable=request.GET['field_selected']
    AllDetails= GetAJob.objects.filter(Field=field_variable)
    return render(request,'FirstApp/GetAJobDetail.html',{'AllDetails':AllDetails,'Field':field_variable})

def NewPageView(request):
    return render(request,'FirstApp/NewPage.html')

def NewPageDetailsView(request):
    field_variable=request.GET['field_selected']
    today = datetime.date.today()
    previous_date = today - datetime.timedelta(days=15)
    print(previous_date)
    print(type(previous_date))
    AllDetails=Professional_Resources.objects.filter(Field=field_variable).filter(Released_On__lt=previous_date)
    return render(request,'FirstApp/NewPageDetails.html',{'AllDetails':AllDetails,'Field':field_variable})

def CommentsandSuggestionsView(request):
    form=CommentsandSuggestionsForm()

    if request.method=='POST':
        form=CommentsandSuggestionsForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            print("inside form sections")
            return render(request,'FirstApp/CommentsandSuggestions.html',{'forms':form,'message':"Your suggestions and comments have been recorded."})

    return render(request,'FirstApp/CommentsandSuggestions.html',{'forms':form})
