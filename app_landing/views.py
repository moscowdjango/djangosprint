from django.shortcuts import render
import models

def index(request):
    return render(request, 'index.html', {
        'blocks': models.Block.objects.all(),
        'highlights': models.Highlight.objects.all(),
    })

