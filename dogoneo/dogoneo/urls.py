from django.contrib import admin
from django.urls import path
from shelter import views as shelter_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shelter_views.dog_list)
]
