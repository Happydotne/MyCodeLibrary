from django.conf.urls import url
from .views import reg

urlpatterns = [
    url(r'^reg$', reg),
]