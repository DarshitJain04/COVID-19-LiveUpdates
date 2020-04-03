from django.db import models

class Corona(models.Model):
	country = models.CharField(max_length=100)

	def __str__(self):
		return self.country

	class Meta:
		verbose_name_plural = 'countries'