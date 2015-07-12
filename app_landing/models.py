from django.db import models

class Block(models.Model):
  title = models.CharField(max_length = 100)

