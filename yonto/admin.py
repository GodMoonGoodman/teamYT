from django.contrib import admin

from yonto.models import *

class MileResultAdmin(admin.ModelAdmin):
	list_display = ('rank', 'mileage', 'result')

class CourseAdmin(admin.ModelAdmin):
	list_display = ('title', 'hakgi')

admin.site.register(MileResult, MileResultAdmin)
admin.site.register(Course, CourseAdmin)