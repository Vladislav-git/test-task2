from django.db import models


class NumberList(models.Model):

	number_list = models.TextField()

	CHOICES = [
	('BubleSort','BubleSort'),
	('InsertionSort','InsertionSort'),
	('MergeSort','MergeSort')]

	algorithm = models.CharField(max_length=20, choices=CHOICES)

	sorted_list = models.TextField()

	file_field = models.FileField(null=True, blank=True)

