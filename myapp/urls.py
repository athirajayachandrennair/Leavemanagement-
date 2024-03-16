from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view,name="view"),
    path('viewinsert/', views.viewinsert,name="viewinsert"),
    path('detailview/<str:pk>', views.detailview,name="detailview"),
    path('', views.insert,name="insert"),
    path('about/', views.hii,name="hii"),
     path('index/', views.index,name="index"),
    #   path('login/', views.login,name="login"),
    #   path('loguser/',views.loguser,name='loguser'),
     path('loggeduser/',views.loggeduser,name='loggeduser'),
    #  path('loginuser/',views.loginuser,name='loginuser'),
     path('log/',views.log,name='log'),
    #  path('signup',views.signup,name='signup')
      # path('loguser1/',views.loguser1,name='loguser1'),
    


   
   
]