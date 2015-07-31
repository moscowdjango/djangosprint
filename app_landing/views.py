from django.shortcuts import render
import models

def index(request):
    return render(request, 'index.html', {
        'blocks': models.Block.objects.all(),
        'highlights': models.Highlight.objects.all(),
        'scheduleItems': models.ScheduleItem.objects.all(),
        'organizers': models.Organizer.objects.all(),
        'sponsors': models.Sponsor.objects.all(),
    })

