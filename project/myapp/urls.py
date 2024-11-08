from django.urls import path
from myapp import views


urlpatterns = [ 
               
    path('', views.signin, name="signin"),
    path('signup/',views.signup, name="signup"),
    path('home/',views.home, name="home"),
    path('create/',views.create, name="create"),
   
    path('update/<int:id>/',views.update,name="update"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('p/',views.popup,name="popup"),
    
    
    path('post/<int:id>/',views.post,name="post"),
    path('read/',views.retrieve,name="retrieve"),
]


