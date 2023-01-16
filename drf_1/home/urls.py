from django.urls import path,include
from home import views
urlpatterns = [
    # path('', views.home, name="home"),
    # path('stucreate/', views.student_create, name="stucreate"),
    path('studentapi/', views.student_api, name="studentapi"),
    
]
