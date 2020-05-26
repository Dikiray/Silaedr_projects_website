from django.conf.urls import url
from dappx import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('delete_project/<str:name>/', views.delete_project),
    path('project/<str:name>/',views.project),
    url('create_new_project/',views.create_new_project,name="create_new_project"),
    url('register/',views.register,name='register'),
    url('user_login/',views.user_login,name='user_login'),
]
