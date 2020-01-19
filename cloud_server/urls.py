from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from basic.views import make_entries

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', make_entries, name="home")
]
