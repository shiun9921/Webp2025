from django.urls import path
from.import views

urlpatterns = [
    path('add', views.add_post, name='add_post'),
    path('list', views.list_post, name='list_post'),
]

#urlpatterns = [
#    path('', views.HelloApiView.as_view(), name='Index'),
#    path('list', views.list_post, name='list_post'),
#]

