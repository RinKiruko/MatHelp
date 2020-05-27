from django.urls import path
from django.views.generic import RedirectView

from distribution.views import Distribute

app_name = 'distribution'
urlpatterns = [
    path('settings/', RedirectView.as_view(pattern_name='crud:statement-list'), name='settings'),
    path('distribute/<int:year>/<int:month>/', Distribute.as_view(), name='distribute'),
]
