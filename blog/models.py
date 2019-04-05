from django.db import models

# Create your models here.
class Blog(models.Model):
    Title = models.CharField(max_length = 100)
    Pub_date = models.DateTimeField()
    image = models.ImageField(upload_to = 'images/')
    Body = models.TextField()


    def summary(self):
    	return self.Body[:60]

    def Pub_date_pretty(self):
    	return self.Pub_date.strftime('%b %e %Y')

    def __str__(self)	:
    	return self.Title