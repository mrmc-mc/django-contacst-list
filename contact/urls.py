from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app = "api"
urlpatterns = [
    path('contacts',views.ContactView.as_view(), name="list"),
    path('person/<int:pk>',views.ContactDetail.as_view(), name="detail")
]

urlpatterns = format_suffix_patterns(urlpatterns)