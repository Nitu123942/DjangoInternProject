from django.db import models
from course.models import Course
from certification.models import Certification

class CourseCertificationMapping(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    certification = models.ForeignKey(Certification, on_delete=models.CASCADE)
    primary_mapping = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('course', 'certification')

    def __str__(self):
        return f"{self.course.name} - {self.certification.name}"
    
