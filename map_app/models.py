from django.db import models


# Create your models here.
class Income(models.Model):
	district_code = models.CharField(max_length=50)
	district_name = models.CharField(max_length=200)
	month = models.IntegerField()
	income_by_month = models.CharField(max_length=200)
	income_last_month = models.FloatField()
	income_difference = models.FloatField()
	income = models.FloatField()
	
	# def __str__(self):
	# 	return "{} ({}) total  : ".format(self.district_name, self.district_code)
	
	def save(self, *args, **kwargs):
		try:
			self.income, self.income_last_month, self.income_difference = round(self.income, 2), round(
				self.income_last_month, 2), abs(round(self.income_difference, 2))
			self.income = 0 if self.income < 0 else self.income
			self.income_last_month = 0 if self.income_last_month < 0 else self.income_last_month
			self.income_difference = 0 if self.income_difference < 0 else self.income_difference
			self.month = 1 if self.month < 0 else self.month
			super().save(*args, **kwargs)
		except TypeError as te:
			pass

# class DistrictInfo(models.Model):
