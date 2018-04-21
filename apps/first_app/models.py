from __future__ import unicode_literals
from django.db import models


class CourseManager(models.Manager):
    def course_manager(self, postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = "Course name must be at least 5 characters long"
        return errors



class Course(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CourseManager()


class DescriptionManager(models.Manager):
    def description_manager(self, postData):
        errors = {}
        if len(postData['description']) < 15:
            errors['description'] = 'Course description must be at least 15 characters long'
        return errors

class Description(models.Model):
    desc = models.TextField()
    describing = models.OneToOneField(Course, on_delete=models.CASCADE, related_name='described_by')
    objects = DescriptionManager()
# Create your models here.
