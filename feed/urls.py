from django.urls import path
from . import views
from django.views.generic.detail import DetailView

app_name = 'feed'

urlpatterns = [
    path("", views.HomePage.as_view(), name='index'),
    path("<int:pk>/", views.PostDetailView.as_view(), name='detail'),
    path("new/", views.CreateNewPost.as_view(), name='new_post'),
]
