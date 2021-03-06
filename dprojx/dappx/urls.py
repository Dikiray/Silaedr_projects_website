from django.conf.urls import url
from dappx import views
from django.urls import path

app_name = 'dappx'
urlpatterns=[
    path('project/<str:name>/',views.project),
    url('create_new_project/',views.create_new_project,name="create_new_project"),
    url('user_login/',views.user_login,name='user_login'),
    url('review/',views.review,name="review"),
]
