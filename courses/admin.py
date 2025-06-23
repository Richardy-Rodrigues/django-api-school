from django.contrib import admin

from . import models

@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'created', 'updated', 'active')


@admin.register(models.Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'email', 'evaluation', 'created', 'updated', 'active')
