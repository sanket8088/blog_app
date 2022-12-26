from django.db import models

class Reaction(models.Model):
    reaction_type = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    created_at = models.DateTimeField(auto_now_add=True)