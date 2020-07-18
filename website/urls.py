from django.urls import path
from website import views
app_name ='website'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('contato/', views.contato, name='contato'),
    path('sobre/', views.sobre, name='sobre')
]
