from django.urls import path
from website import views


urlpatterns = [
    path('', views.post_list, name='post_list'),

]