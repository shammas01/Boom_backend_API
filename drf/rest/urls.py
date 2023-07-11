from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    # TokenRefreshView,
)

urlpatterns = [
    path('',views.endpoind),
    path('advocate/',views.advocate_list,name='advocate'),
    path('advocate/<str:username>/',views.AdvocateDetails.as_view()),
    path('company/',views.company_list,name='advocate'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),


    # path('advocate/<str:username>/',views.advocate_details),  
]