from django.shortcuts import render

def index(request):
    from django.apps import apps
    print(apps.get_app_config('app_landing').verbose_name)
    return render(request, 'index.html')

