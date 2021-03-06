from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

urlpatterns = [
    path('', LoginView.as_view()),

    path('crud/', include('crud.urls', namespace='crud')),
    path('distribution/', include('distribution.urls', namespace='distribution')),

    path('admin/', admin.site.urls),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
