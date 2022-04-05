from django.urls import path
from .views import IndexView

app = 'home'
urlpatterns = [
    path('', IndexView.as_view(), name='index')
]
