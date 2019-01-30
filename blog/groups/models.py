from django.db import models

# Create your models here.

class Person(models.Model):

	first_name = models.CharField(max_length = 70)
	second_name = models.CharField(max_length = 70)

	def __str__(self):
		return '{0} {1}'.format(self.second_name, self.first_name)


class Group(models.Model):
	
	name = models.CharField(max_length = 120)
	members = models.ManyToManyField(Person, through = 'Membership')

	def __str__(self):
		return self.name

class Membership(models.Model):

	person = models.ForeignKey(Person, on_delete = models.CASCADE, related_name = 'groups')
	group = models.ForeignKey(Group, on_delete = models.CASCADE)
	date_joined = models.DateField(auto_now = True)
	invite_reason = models.CharField(max_length = 300)

	def __str__(self):
		return f'{self.group} {self.person} {self.invite_reason}'




