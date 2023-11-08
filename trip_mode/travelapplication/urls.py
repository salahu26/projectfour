
from django.urls import path,include

from . import views
urlpatterns = [

    path('',views.trail,name='demo'),
#    path('about/', views.about, name='anyname'),
 #   path('content/', views.content, name='opps'),
   # path('addp/',views.addition,name='poiu')
 #    path('',views.fun_static,name='demo')
]