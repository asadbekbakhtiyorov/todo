from django.contrib import admin
from django.urls import path
from new2 import views
from new2.views import *

urlpatterns = [
    #####################home_page###########################################
    path('todo/', all_todos, name="todo"),
    ####################give id no. item_id name or item_id=i.id ############
    path('del/<int:son>', remove, name="del"),
    ########################################################################
    path('admin/', admin.site.urls),
    path('todo/submit', views.index, name='submit' ),
    path('', views.loginView, name='login'),
    path('reg/', registration, name='reg'),
    path('logout/', LogoutView, name='logout')
]
