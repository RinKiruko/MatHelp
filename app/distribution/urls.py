from django.urls import path

from distribution.views import *

app_name = 'distribution'
urlpatterns = [
    path('settings/', Settings.as_view(), name='settings'),
    path('distribute/<int:year>/<int:month>/', Distribute.as_view(), name='distribute'),
]
