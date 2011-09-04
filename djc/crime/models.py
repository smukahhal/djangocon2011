from django.contrib.gis.db import models

class Crime(models.Model):
	crime_type = models.CharField(max_length=50)
	date_time = models.DateTimeField()
	description = models.TextField()

	pt = models.PointField()

	objects = models.GeoManager()
