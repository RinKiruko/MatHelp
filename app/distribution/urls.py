from django.urls import path

from distribution.views import *

app_name = 'distribution'
urlpatterns = [
    path('settings/', Settings.as_view(), name='settings'),
    path('distribute/', Distribute.as_view(), name='distribute'),
]
