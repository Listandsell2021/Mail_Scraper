from django.db import models

class Websites_Model(models.Model):
    website_name = models.CharField(max_length=250)
    def __str__(self):
        return self.website_name
