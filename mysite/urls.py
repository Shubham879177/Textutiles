from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze', views.analyze, name='analyze')


]
    
    # path('capfirst',views.capfirst, name = "capitalize"),
    # path('newlineremove',views.newlineremove, name = "newlineremove"),
    # path('spaceremover',views.spaceremover, name = "spaceremover"),
    # path('charcount',views.charcount, name = "charcount"),
    