from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *
from . import views
urlpatterns = [
    path("", views.MemberList.as_view()), 
    path('<int:pk>/', views.MemberDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)