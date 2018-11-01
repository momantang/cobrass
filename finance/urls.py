from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cronjob', views.CronjobView.as_view(), name='cronjob'),
    path('update_cronjob', views.update_cronjob, name='update_cronjob'),
    path('html/<str:page>/', views.html_page)
]
