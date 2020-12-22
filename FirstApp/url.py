from django.conf.urls import url
from FirstApp import views

app_name='FirstApp'

urlpatterns=[
  url(r'^Personal_Development/$',views.Personal_Development,name='Personal_Development'),
url(r'^Professional_Development/$',views.Professional_Development,name='Professional_Development'),
url(r'^Financial_Success/$',views.Financial_Success,name='Financial_Success'),

url(r'^AddResource/$',views.AddResourceView,name='AddResource'),

url(r'^Add_Personal_Development_Resource/$',views.AddPersonalDevelopmentResourceView,name='Add_Personal_Development_Resource'),
url(r'^FinancialSuccess/$',views.FinancialSuccessView,name='Financial_Success'),
url(r'^Add_Financial_Success_Resource/$',views.Add_Financial_Success_ResourceView,name='Add_Financial_Success_Resource'),
url(r'^Registration/$',views.RegistrationView,name='Registration'),
url(r'^user_login/$',views.user_login,name='user_login'),
url(r'^MyGoal/$',views.MyGoalView,name='MyGoal'),
url(r'^MyLibrary/$',views.MyLibraryView,name='MyLibrary'),
url(r'^Challenge/$',views.ChallengeView,name='Challenge'),
url(r'^Challenge1/$',views.Challenge1View,name='Challenge1'),
url(r'^Challenge2/$',views.Challenge2View,name='Challenge2'),
url(r'^AdvicePathsExperienceResources/$',views.AdvicePathsExperienceResourcesView,name='AdvicePathsExperienceResources'),
url(r'^AddExperience/$',views.AddExperienceView,name='AddExperience'),
url(r'^ThePage/$',views.ThePageView,name='ThePage'),
url(r'^GetAJob/$',views.GetAJobView,name='GetAJob'),
url(r'^GetAJobDetail/$',views.GetAJobDetailView,name='GetAJobDetail'),
url(r'^NewPage/$',views.NewPageView,name='NewPage'),
url(r'^NewPageDetails/$',views.NewPageDetailsView,name='NewPageDetails'),
url(r'^CommentsAndSuggestions/$',views.CommentsAndSuggestionsView,name='CommentsAndSuggestions'),
url(r'^AboutUs/$',views.AboutUsView,name='AboutUs'),
url(r'^ShareUs/$',views.ShareUsView,name='ShareUs'),
url(r'^ContactUs/$',views.ContactUsView,name='ContactUs'),
url(r'^Share1/$',views.Share1View,name='Share1'),
url(r'^ApplyJob/$',views.ApplyJob,name='ApplyJob'),
url(r'^AddJobPortal/$',views.AddJobPortal,name='AddJobPortal'),
url(r'^CompanyAndStartup/$',views.CompanyAndStartup,name='CompanyAndStartup'),
url(r'^AddCompanyAndStartup/$',views.AddCompanyAndStartup,name='AddCompanyAndStartup'),
url(r'^ListOfCompanyOrStartup/$',views.ListOfCompanyOrStartup,name='ListOfCompanyOrStartup'),
url(r'^Review/',views.reviewSite,name='review'),


]
