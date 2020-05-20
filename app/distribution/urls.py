from django.urls import path
from django.views.generic import RedirectView

app_name = 'distribution'
urlpatterns = [
    path('settings/', RedirectView.as_view(pattern_name='crud:statement-list'), name='settings'),
]
