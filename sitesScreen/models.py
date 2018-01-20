from django.db import models

# Create your models here.

class Stuff(models.Model):
	Site_Name = models.TextField(blank = True , null = True)
	A_Value = models.DecimalField(max_digits=5, decimal_places=2)
	B_Value = models.DecimalField(max_digits=5, decimal_places=2)
	Date = models.DateField()