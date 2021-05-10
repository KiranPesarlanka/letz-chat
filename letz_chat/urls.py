from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='chat_app/index.html')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), # <--
    path('logout/', views.logout),
]
