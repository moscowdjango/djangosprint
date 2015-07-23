from django.db import models

class Block(models.Model):

    class Type(object):
        NONE = 'none'
        ABOUT = 'about'
        SCHEDULE = 'schedule'
        ORGANIZERS = 'organizers'
        SPONSORS = 'sponsors'
        MAP = 'map'

    type = models.CharField(default = Type.NONE, max_length = 50, choices = (
        (Type.NONE, "none"),
        (Type.ABOUT, "about"),
        (Type.SCHEDULE, "schedule"),
        (Type.ORGANIZERS, "organizers"),
        (Type.SPONSORS, "sponsors"),
        (Type.MAP, "map"),
    ))
    
    title = models.CharField(default="", max_length = 100)
    order = models.IntegerField(default = 0)
    content = models.TextField(default = "");

