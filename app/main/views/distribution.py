from django.views.generic import View


class Distribute(View):
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
