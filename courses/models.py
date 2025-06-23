from django.db import models

# Abstract Model
class Base(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

# Course Model
class Course(Base):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    class Meta:
        verbose_name  = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.title

# Evaluation Model    
class Evaluation(Base):
    course = models.ForeignKey(Course, related_name='evaluations', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    evaluation = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = 'Evaluation'
        verbose_name_plural = 'Evaluations'
        unique_together = ['email', 'course'] # Does not allow an email linked to more than one course
    
    def __str__(self):
        return f"{self.name} rated the course {self.course} with a score {self.evaluation}"