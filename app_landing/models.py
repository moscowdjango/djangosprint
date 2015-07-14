from django.db import models

class Block(models.Model):

    class Type(object):
        NONE = 'none'
        ABOUT = 'about'
        SCHEDULE = 'schedule'

    type = models.CharField(default = Type.NONE, max_length = 50, choices = (
        (Type.NONE, "none"),
        (Type.ABOUT, "about"),
        (Type.SCHEDULE, "schedule"),
    ))
    title = models.CharField(max_length = 100)

