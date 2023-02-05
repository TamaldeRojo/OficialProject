from django.urls import path
from .views import Homeview

urlpatterns = {
    path('',Homeview ),
}
