from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.ProfileDetailView.as_view(), name='profile-page'),
]
