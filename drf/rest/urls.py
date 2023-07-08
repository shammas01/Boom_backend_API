from django.urls import path
from . import views

urlpatterns = [
    path('',views.endpoind),
    path('advocate/',views.advocate_list,name='advocate'),
    path('advocate/<str:username>/',views.AdvocateDetails.as_view()),
    path('company/',views.company_list,name='advocate'),


    # path('advocate/<str:username>/',views.advocate_details),  
]