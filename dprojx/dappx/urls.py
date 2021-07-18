from django.conf.urls import url
from dappx import views
from django.urls import path

app_name = 'dappx'
urlpatterns=[
    path('project/<str:name>/',views.project),
    path('delete/<str:name>/', views.delete_project),
    path('en_project/<str:name>/', views.en_project),
    path('change_project/<str:name>/', views.change_project),
    url('create_new_project/',views.create_new_project,name="create_new_project"),
    url('en_index/', views.en_views, name="en_index"),
    url('user_login/',views.user_login,name='user_login'),
    url('review/',views.review,name="review"),
]
