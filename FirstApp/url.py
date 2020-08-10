from django.conf.urls import url
from FirstApp import views

app_name='FirstApp'

urlpatterns=[
  url(r'^Personal_Development/$',views.Personal_Development,name='Personal_Development'),
url(r'^Professional_Development/$',views.Professional_Development,name='Professional_Development'),
url(r'^Financial_Success/$',views.Financial_Success,name='Financial_Success'),
url(r'^Software_Development/$',views.SoftwareDevelopmentView,name='Software_Development'),
url(r'^Backup/$',views.BackupView,name='Backup'),
url(r'^Bank_Po/$',views.Bank_PoView,name='Bank_Po'),
url(r'^Business/$',views.BusinessView,name='Business'),
url(r'^CAT/$',views.CATView,name='CAT'),
url(r'^Database_View/$',views.DatabaseView,name='Database'),
url(r'^GMAT/$',views.GMATView,name='GMAT'),
url(r'^IAS/$',views.IASView,name='IAS'),
url(r'^Linux/$',views.LinuxView,name='Linux'),
url(r'^Medical/$',views.MedicalView,name='Medical'),
url(r'^SSC_CGL/$',views.SSC_CGLView,name='SSC_CGL'),
url(r'^Storage/$',views.StorageView,name='Storage'),
url(r'^Swimming/$',views.SwimmingView,name='Swimming'),
url(r'^Wintel/$',views.WintelView,name='Wintel'),
url(r'^Law/$',views.LawView,name='Law'),
url(r'^Networking/$',views.NetworkingView,name='Networking'),
url(r'^AddResource/$',views.AddResourceView,name='AddResource'),
url(r'^Brian_Tracy/$',views.BrianTracyView,name='Brian_Tracy'),
url(r'^Deepak_Chopra/$',views.DeepakChopraView,name='Deepak_Chopra'),
url(r'^Earl_Nightingale/$',views.EarlNightingaleView,name='Earl_Nightingale'),
url(r'^Jack_Canfield/$',views.JackCanfieldView,name='Jack_Canfield'),
url(r'^Jim_Rohn/$',views.JimRohnView,name='Jim_Rohn'),
url(r'^Napolean_Hill/$',views.NapoleanHillView,name='Napolean_Hill'),
url(r'^Robin_Sharma/$',views.RobinSharmaView,name='Robin_Sharma'),
url(r'^Shiv_Khera/$',views.ShivKheraView,name='Shiv_Khera'),
url(r'^Steven_R_Covey/$',views.StevenRCoveyView,name='Steven_R_Covey'),
url(r'^Tony_Robbins/$',views.TonyRobbinsView,name='Tony_Robbins'),
url(r'^Wayne_Dyer/$',views.WayneDyerView,name='Wayne_Dyer'),
url(r'^Zig_Ziglar/$',views.ZigZiglarView,name='Zig_Ziglar'),
url(r'^Add_Personal_Development_Resource/$',views.AddPersonalDevelopmentResourceView,name='Add_Personal_Development_Resource'),
url(r'^BrianTracyFinancialSuccess/$',views.BrianTracyFinancialSuccessView,name='BrianTracyFinancialSuccess'),
url(r'^RobertKiyosakiFinancialSuccess/$',views.RobertKiyosakiFinancialSuccessView,name='RobertKiyosakiFinancialSuccess'),
url(r'^TonyRobbinsFinancialSuccess/$',views.TonyRobbinsFinancialSuccessView,name='TonyRobbinsFinancialSuccess'),
url(r'^OtherFinancialSuccess/$',views.OtherFinancialSuccessView,name='OtherFinancialSuccess'),
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


]
