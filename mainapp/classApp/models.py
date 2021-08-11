from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    course_number = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)
    instructor_name = models.CharField(max_length=60, default="", blank=True)
    duration = models.DecimalField(default=0.00, max_digits=10000, decimal_places=2)

    SUBJECTS = {
        ('math', 'math'),
        ('science', 'science'),
        ('spanish', 'spanish'),
    }

    objects = models.Manager()

    def __str__(self):
        return self.name