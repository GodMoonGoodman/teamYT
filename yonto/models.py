from django.db import models

# Create your models here.


class Course(models.Model):
	hakgi= models.SmallIntegerField('hakgi', null=False, blank=False)
	hakno= models.CharField('hakno', max_length=10, null=False, blank=False)
	bb = models.CharField('bb', max_length=2, null=False, blank=False)
	sbb = models.CharField('sbb', max_length=2, null=False, blank=False)
	title = models.CharField('title', default="", max_length=20, null=False)
	room = models.CharField('room',max_length=10, blank=False)
	max_student = models.SmallIntegerField('max_student', null=False, blank=False)
	participation = models.SmallIntegerField('participation', null=False, blank=False)
	min_mile = models.SmallIntegerField('min_mile', null=False, blank=False)
	max_mile = models.SmallIntegerField('max_mile', null=False, blank=False)
	avr_mile = models.SmallIntegerField('avr_mile', null=False, blank=False)
	professor = models.CharField('prof',max_length=10)
	credit = models.SmallIntegerField('credit')

	analysis = models.BooleanField('isAnalysis', null=False, blank=False)

	def __str__(self):
		return self.title

class MileResult(models.Model):
	rank = models.SmallIntegerField('rank', null=False, blank=False)
	mileage = models.SmallIntegerField('mileage', null=False, blank=False)
	isMajor = models.BooleanField('isMajor', null=False, blank=False)
	numEnroll = models.SmallIntegerField('numEnroll', null=False, blank=False)
	graduation = models.BooleanField('isMajor', null=False, blank=False)
	first = models.BooleanField('first', null=False, blank=False)
	credit = models.SmallIntegerField('mileage', null=False, blank=False)
	prev = models.FloatField('prev', null=False, blank=False)
	grade = models.SmallIntegerField('grade', null=False, blank=False)
	result = models.BooleanField('result', null=False, blank=False)
	course = models.ForeignKey(Course, null=False , default=None)

	def __str__(self):
		return self.rank


class Custom_User(models.Model):
	email = models.CharField('email',max_length=30)
	password = models.CharField('pass',max_length=10)
	is_active = models.BooleanField('is_active', null=False, blank=False)

	def __str__(self):
		return self.email