from django.contrib import admin
from django.urls import path, include
from todolist import views as dip_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', include('todolist.urls')),
    path('account/', include('users_app.urls')),
    path('', dip_views.index, name='index'),
    path('contact', dip_views.contact, name='contact'),
    path('about', dip_views.about, name='about'),
]
    
